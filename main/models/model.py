from flask import json
import datetime

USERS=[] #global variable for users.

class User:
    """class for user registration"""

    def __init__(self, user_id, firstname, lastname, othernames, username, email, phonenumber, password, isAdmin):
          # initialise the variables for this class here
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.username = username
        self.phonenumber = phonenumber
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        self.registered_on = datetime.datetime.now()
        self.users_list = []

    def register(self, user_id, firstname, lastname, othernames, username, email, phonenumber, password, isAdmin):
        """this function is for creating a new user. the fuction returns a boolean true if a user has been
        successfully registered and false if otherwise."""
        oldUsersListLength = len(self.users_list) # lets store the length of users_list before appending a new user.
        print(self.users_list != None)
        if self.users_list:
            for user in self.users_list:
                for vals in user.values():
                    if user_id not in vals:
                        #create the list below with precise indexing as illustrated below
                        # { user_id:[[0]= firstname, [1]= secondname, [2]=lastname,[3]othernames, [4] = username, [5] = phonenumber, [6] = email, [7] = password, [8] = isAdmin] }
                        self.users_list.append({user_id:[firstname,lastname,othernames,username, phonenumber, email, password, isAdmin]})
                        if len(self.users_list) > oldUsersListLength:
                            return True #'user added' # user was created successfully.
                        else:
                            return False # user was not created.
                    else:
                        self.users_list.append({user_id:[firstname,lastname,othernames,username, phonenumber, email, password, isAdmin]})
                        return True
        else:
            self.users_list.append({user_id:[firstname,lastname,othernames,username, phonenumber, email, password, isAdmin]})
            return True

    def checkUsernameExists(self, username):
        """helper function to check whether username Exists before registering a new user. this function returns
        a boolean true if the username already exists and false if the username is not yet used."""        
        #lets loop through this global users_list and append all usernames to list availUsernames
        availUsernames=[]        
        
        if USERS:
            for items in USERS:
                for values in items.values():
                    availUsernames.append(values[4]) #index 4 holds our usernames by default.
                    if username not in availUsernames:
                        return False #false will mean they dont exist
                    else:
                        return True # this will mean they exist
        else:            
            print(availUsernames)
            return False  
    # def __str__(self):
    #     return "user: {} firstname:{} lastname:{} othernames:{} username:{} phonenumber:{} with email {}:isadmin:{}".format(self.user_id ,self.firstname,self.lastname,self.othernames,self.username,
    #     self.phonenumber,self.email, self.isAdmin)


class Redflag:
    """
    class for creating a redflag post 
    """

    def __init__(self, redflag_id, user_id, description, email, status, location, createdby, createdOn):
        self.redflag_id = redflag_id
        self.user_id = user_id
        self.description = description
        self.email = email
        self.status = self.status()[0]
        self.location = location
        self.createdOn =  datetime.datetime.now()
        self.createdby = createdby
        
    def __str__(self):
        return "redflag_id:{} user_id:{} description:{} email:{} location:{} createdby:{} createdOn:{} status:{} ".format(self.user_id,self.redflag_id,self.description,self.email,self.location,self.createdOn, self.createdby, self.status)

    def status(self):
        """
        Generate status list for parcel orders
        """
        status = ['draft','rejected', 'resolved', 'under_investigation']
        return status


