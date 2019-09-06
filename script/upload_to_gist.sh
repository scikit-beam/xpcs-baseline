USERNAME=bnl-dama-bot
GIST_ID=495b52d09a9e30a7c4b0f4c0d104b9c7
set -e
git clone https://${USERNAME}:${GITHUB_OAUTH_TOKEN}@gist.github.com/${USERNAME}/${GIST_ID} gist
cd gist
for file in $*
do
    # Make a filename that is unique and contains some identifying info.
    FILENAME=artifact-${TRAVIS_COMMIT}-${TRAVIS_BUILD_NUMER}-${TRAVIS_BUILD_ID}-${file}
    cp ../${file} ${FILENAME}
    git add "${FILENAME}"
done
git commit -am "Artifacts from Travis build number ${TRAVIS_BUILD_NUMBER}

TRAVIS_COMMIT=${TRAVIS_COMMIT}
TRAVIS_BUILD_NUMBER=${TRAVIS_BUILD_NUMBER}
TRAVIS_BUILD_ID=${TRAVIS_BUILD_ID}"
git push origin master
