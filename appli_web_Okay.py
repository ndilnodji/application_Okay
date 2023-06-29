import numpy as np
import streamlit as st 
import pickle

    
# loading in the model to predict on the data  
open_model = open('model.pkl', 'rb')  
load_model= pickle.load(open_model)
##chargement du Model
#model_charge=pkl.load(open('mon_model.sav','rb'))

def prix_voiture(input_data):
    input_data_numpy=np.asarray(input_data)
    input_data_reshape= input_data_numpy.reshape(1,-1)
    prediction=model_charge.predict(input_data_reshape)
    return prediction[0]

def main():
    st.title('BIENVENUE SUR LE SITE DE PREDICTION DES PRIX DES VOITURES') 
    
    Manufacturer=st.number_input('Entrez le nom du Fabriquant')  
    Model=st.number_input('Entrez le Model de la voiture ') 
    annee_prod=st.number_input('Entrez l\'annee de fabrication de la voiture') 
    Category=st.number_input('Entrez la categorie de la voiture') 
    Leathere_interior=st.number_input('la voiture a t\'elle un confort interieur?') 
    Fuel_type=st.number_input('entrez le type du moteur de la voiture') 
    Engine_volume =st.number_input('Entrez le volume du moteur')
    #genre = st.radio("What's your favorite movie genre",
    #('Comedy', 'Drama', 'Documentary'))
    #latitude= st.number_input("Choisir la latitude ", min_value=data['lat'].min(),max_value=data['lat'].max())
    #longitude= st.number_input("Choisir la longitude ", min_value=data['lon'].min(),max_value=data['lon'].max())
    #st.write('Vos coordonnées GPS (latitude,longitude) : ', (latitude,longitude))
    Mileage =st.number_input('Entrez le Mileage')
    Cylinders =st.number_input('Entrez le Cylinders de la voiture')
    Gear_box_type=st.number_input('Entrez le Gear box types de la voiture')
    Drive_wheels =st.number_input('Entrez le Drive_wheels')
    Doors =st.number_input('Entrez le nombre des portieres ')
    Wheel =st.number_input('Entrez la postion des volants')
    Color =st.number_input('Entrez la couleur de la voiture')
    Airbags =st.number_input('Entrez Airbags')

    predir=''
                               
    if st.button('Resultat') :
        predir=prix_voiture([Manufacturer,Model,annee_prod,Category,Leathere_interior,Fuel_type ,Engine_volume,Mileage,Cylinders,Gear_box_type,Drive_wheels,Doors,Wheel,Color,Airbags])


    st.success(predir)
                                    
if __name__=='__main__':
    main()