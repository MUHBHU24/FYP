import { defineStore } from 'pinia'
import axios from 'axios'

// Define the 'userAuth' store
export const useAuthUserStore = defineStore({
     id: 'userAuth',
    
     // Define the initial state of the userInfo object
     state: () => ({
        userInfo: {
            id : null,
            username: null,
            accessToken: null,
            refreshToken: null,
            isAuthenticated: false,
        }
    }),

    actions: {
        // Initialise the user store with values from localStorage
        setupStore() {
            // Check if 'userInfo.access' exists in localStorage
            if (localStorage.getItem('userInfo.access')) {
                // Set userInfo object properties from localStorage
                this.userInfo.id = localStorage.getItem('userInfo.id')
                this.userInfo.username = localStorage.getItem('userInfo.username')
                this.userInfo.accessToken = localStorage.getItem('userInfo.access')
                this.userInfo.refreshToken = localStorage.getItem('userInfo.refresh')
                this.userInfo.isAuthenticated = true

                // Call updateToken function to refresh the user's token
                this.updateToken() 

                // Log a message indicating the user is authenticated
                console.log('The user: ' + this.userInfo + ' is authenticated')
            }
        },

        // Create a new user and store the user's ID and username
        createUser(userInfo) {
            console.log('Creating user', userInfo)

            // Set userInfo properties based on the input userInfo
            this.userInfo.id = userInfo.id
            this.userInfo.username = userInfo.username

            // Save the ID and username to localStorage
            localStorage.setItem('userInfo.id', this.userInfo.id)
            localStorage.setItem('userInfo.username', this.userInfo.username)

            console.log('User created', this.userInfo)
        },

        // Create and store a new user token
        createToken(data) {
            console.log('Creating token', data)

            // Set the userInfo properties for accessToken and refreshToken
            this.userInfo.accessToken = data.accessToken
            this.userInfo.refreshToken = data.refreshToken
            this.userInfo.isAuthenticated = true

            // Save the accessToken and refreshToken to localStorage
            localStorage.setItem('userInfo.access', data.accessToken)
            localStorage.setItem('userInfo.refresh', data.refreshToken)
        },

        // Update the user's access token by requesting a new token using the refresh token
        updateToken() {
            // Make an axios POST request to refresh the user's access token
            axios.post('/api/survey/refresh/', {
                refresh: this.userInfo.refreshToken
            })
            .then((response) => {
                console.log('Token updated', response.data)

                // Update the userInfo.accessToken with the new access token from the response
                this.userInfo.accessToken = response.data.accessToken

                // Save the new accessToken to localStorage
                localStorage.setItem('userInfo.accessToken', response.data.accessToken)

                // Set the Authorization header for axios requests to include the new access token
                axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.accessToken
            })
            .catch((error) => {
                console.log(error)

                // If there's an error, call deleteToken() to remove the user's tokens and reset authentication status
                this.deleteToken()
            })
        },

        // Delete the user token and reset user authentication status
        deleteToken() {
            console.log('Removing token')

            // Reset userInfo properties related to authentication
            this.userInfo.id = false
            this.userInfo.username = false
            this.userInfo.accessToken = null
            this.userInfo.refreshToken = null
            this.userInfo.isAuthenticated = false

            // Remove the related keys from localStorage
            localStorage.removeItem('userInfo.id')
            localStorage.removeItem('userInfo.username')
            localStorage.removeItem('userInfo.accessToken')
            localStorage.removeItem('userInfo.refreshToken')
            localStorage.removeItem('userInfo.isAuthenticated')
        },
    },
})