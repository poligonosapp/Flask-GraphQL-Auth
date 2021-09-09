from auth0.v3.authentication import Social

from poligonosapp-github-flask-consumer import app

#pipelines GitHub Python Flask Auth

def new_function(){
    auth0domain = app.cconfig['AUTH0_PYTHON_CLIENT_ID']
    return auth0domain;
}

auth0_python_client_id = new_function();

def github_auth(){

    try{
        socialGithub = Social(auth0domain)
        socialGithub.login(client_id=auth0_python_client_id, access_token='repo-token', connection='github')
        print(" GitHub Actions auth0 success ")
        return true;
    }
    finally{
        print(" GitHub Actions auth0 failed ")
        return false;
    } # end finnaly
}

# social = Social('myaccount.auth0.com')
# social.login(client_id='...', access_token='...', connection='atlassian')

# social = Social('myaccount.auth0.com')
# social.login(client_id='...', access_token='...', connection='bitbucket')
