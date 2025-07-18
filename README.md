#### To run the Server from the CLI execute the following command 
uvicorn main:app --reload


#### Overall view of the application
From the main page (landing page) you can select the mathematical formula you want 
and to make it intuitive you have at your disposal boxes with a minimalistic desing 
encompeses the name of the of the mathematical formula/computation you may want.

From there the application dispaly a form like widget that request for the information 
needed for the computation. Input them and press enter of 'compute' button and wait 
for the result to be displayed.

#### Routing and project structure
From the landing page (rount: /math_formulas - name of the microservice base rounting) by choosing each box you are redirected to the '/math_formulas/{name_of_formula}' 

