# Facility Address Project
As part of my internship, I created a Python program that used the Google Maps Api to find the addresses of more than 5000 sports facilities throughout the US. The company agreed that it would be impossible to find the addresses with a 100% accuracy and was only looking to get the addresses to have a rough estimate of where all their facilities were located.

# Plan
I imported an Excel document that contained 5400+ rows with a Facility column and State column (which I didn't upload for privacy reasons). Then I made the Google Maps Api read over every row in this document and return the address for the Facility + State combination, or return "Address not found". I chose to retrieve and save this data in batches of 1000 in case the program crashed. Then I did the same process for the Mapquest Api to cross reference the addresses found and to get a feel of how accurate the data was. When both codes were done running, I used the Google Maps Api to only search for the facility name for the addresses that couldn't be found witht he facility + state combination. At the end of the code, I'm combining all of the batch documents into 1 big document. 

# About Me
I am Kevin de Lange, an Information Systems Management student at Shawnee State University. In previous years I have also obtained a bachelor in Marketing and a bachelor in Business Management. I am looking for a job in the data analyst or business analyst world. If you would like to get in contact with me, please email me at: kevin.delange@hotmail.com
