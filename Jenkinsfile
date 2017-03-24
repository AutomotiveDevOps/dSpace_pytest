#!groovy

pipeline {
    agent any
    options {
        // Only keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr:'10'))
        timestamps()
    }
    stages {
        stage('dSpace Build'){
            steps {
                echo 'Build dSpace Models'
            }
        }
        stage('dSpace Test'){
            steps {
                bat 'py.test'
            }
        }
    }
    post {
        always {
            junit 'test-reports/report.xml'
            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'test-reports',
                reportFiles: 'report.html',
                reportName: 'dSpace HIL Report'
            ]
        }
        success {
          mail to:"me@example.com", subject:"SUCCESS: ${currentBuild.fullDisplayName}", body: "Yay, we passed."
        }
        failure {
          mail to:"me@example.com", subject:"FAILURE: ${currentBuild.fullDisplayName}", body: "Boo, we failed."
        }
    }
}