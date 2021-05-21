/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */

export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'fish-coffee-shop.us', // the auth0 domain prefix
    audience: 'fish-coffee-shop', // the audience set for the auth0 app
    clientId: 'tCKAf6nQrzAm8zCXRllogSAv4UpS2m5p', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application.
  }
};
