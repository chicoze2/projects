# WaiterAPP

This project is an order management system for restaurants; with mobile app, web application and a API.

Using the mobile app, the client assembles the request, the request is sent to the API that stores the information in the database and sends a webSocket to the front-end application, where the requests are summarized.


### Techs Used
* API - Express, TypeScript, MongoDB
* Mobile App - React Native (Typescript)
* Web App - React

### How to run 
`required NodeJS` <br/>
`required MongoDB` 


1. Open terminal
2. Type `yarn install` for each  folder (api, mobile-app, web-application)
3. Change DB addres on `api/src/index.js`
4.  Go into the desired directory (`cd api`, `cd mobile-app`, `cd web-application`)
4. Run `yarn start`