// https://github.com/Rudd-O/shared-jenkins-libraries
@Library('shared-jenkins-libraries@master') _


def skip_tests() {
    return {
        println "Tests skipped"
    }
}

genericFedoraRPMPipeline(null, null, null, null, skip_tests())
