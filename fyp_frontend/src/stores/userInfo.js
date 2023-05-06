import { defineStore } from 'pinia'
import axios from 'axios'

// Define the 'user' store
export const useAuthUserStore = defineStore({
     id: 'userAuth',
    
     // Define the initial state of the user object
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
            // Check if 'user.access' exists in localStorage
            if (localStorage.getItem('user.access')) {
                // Set user object properties from localStorage
                this.user.id = localStorage.getItem('user.id')
                this.user.username = localStorage.getItem('user.username')
                this.user.accessToken = localStorage.getItem('user.access')
                this.user.refreshToken = localStorage.getItem('user.refresh')
                this.user.isAuthenticated = true

                // Call updateToken function to refresh the user's token
                this.updateToken() 

                // Log a message indicating the user is authenticated
                console.log('The user: ' + this.userInfo + ' is authenticated')
            }
        },

    }
})
