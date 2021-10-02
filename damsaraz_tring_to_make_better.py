
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty,NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import sqlite3 as sql
import re
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

movielist="Sadhu_Aur_Shaitaan , Rain_or_Shine , Platinum_Blonde , Shopworn , The_Story_of_Temple_Drake , Jeevan_Naiya , Modern_Times , Sabotage , Second_Chorus , Aarzoo , Prelude_to_War , National_Velvet , Phool , Rattan , Udahir_Path , Conflict , The_Ghost_Lady , Shahjehan , Dil_Ki_Rani , Good_News , Road_to_Rio , Port_of_Call , Red_River , Scott_of_the_Antarctic , Aarzoo , Dastaan , Khilari , Rashomon , Awara , Bahar , Daagh , Road_to_Bali , Aah , Paapi , Black_Widow , Boot_Polish , Ilzaam , Naukri , Seven_Samurai , Ghar_Number_44 , Shri_420 , Udaan_Khatola , Udan_Khatola , Delhi_Mein , Anjaan , Somewhere_in_Delhi , Chhoo_Mantar , Ek_Hi_Raasta , Kismat_Ka_Khel , Qismat_Ka_Khel , 12_Angry_Men , Bharat_Mata , Kathputli , Witness_for_the_Prosecution , Kala_Pani , Hiroshima_Mon_Amour , Insaan_Jaag_Utha , Main_Nashey_Mein_Hoon , Rio_Bravo , Bambai_Ka_Babu , Bombay_Ka_Babu , Barsat_ki_Rat , Dil_Apna_Aur_Preet_Parai , Kaala_Bazaar , The_Thief_of_Baghdad , Psycho , Ganga_Jamuna , Mem_Didi , Mutiny_on_the_Bounty , Sanjuro , Tarzan_Meera_Saathi , Gharbar , Yeh_Raaste_Hain_Pyar_Ke , Ishara , Blood_and_Black_Lace , Woman_in_the_Dunes , Aarzoo , Chemmeen_Lahren , Kapurush_Mahapurush , Khandaan , The_Good_the_Bad_and_the_Ugly , Dil_Diya_Dard_Liya , Chelsea_Girls , Chhoti_Si_Mulaqaat , Humraaz , The_Nude_Restaurant , Point_Blank , Anjam , The_Bliss_of_Mrs._Blossom , Blue_Movie , Bombay_Raat_Ki_Bahon_Mein , Deewana , Enter_the_Game_of_Death , Sangharsh , Sunghursh , Sungharsh , Gali_Gali_Sim_Sim , Marlowe , Pyar_Hi_Pyar , A_Thousand_&_One_Nights , Talaash , The_Love_Factor , Days_and_Nights_in_the_Forest , The_Great_White_Hope , Hollywood_Blue , Ilzaam , Ryans_Daughter , Anand , Kolkata_71 , Karwan , Sharmilee , Murmur_of_the_Heart , Bawarchi , The_Godfather , Sweet_Sugar , Doraemon , Distant_Thunder , Enter_the_Dragon , The_Exorcist , Shaitaanee_Raat , Malicious , Mann_Jeete_Jag_Jeet , Namak_Haram , Zanjeer , Belladonna_of_Sadness , Bruce_Li_Ka_Inteqaam , Chhattis_Ghante , Geeta_Mera_Naam , The_Godfather , The_Holy_Mountain , The_Night_Porter , Deewar , The_Story_of_O , Jaws , One_Flew_Over_the_Cuckoos_Nest , Sholay , Kranti_Ki_Tarangein , Zakhmi , Paris_Ki_Ek_Shyam , Jackson_County_Jail , Taxi_Driver , Bhumika , Teesaree_Prakaar_Kee_Muthabhed , Hum_Kisi_Se_Kum_Nahin , Imaan_Dharam , Saturday_Night_Fever , Submission , Shatranj_Ke_Khiladi , Playing_with_Love , Star_Wars , Empire_of_Passion , Athithi , Badalte_Rishte , Blue_Movie , Don , International_Velvet , Midnight_Express , Satyam_Shivam_Sundaram , Sita_Aur_Gita , Trishul , Ehsaas , Alien , Amardeep , Apocalypse_Now , American_Dragula , Hasino_Ka_Kabila , Kremar_Banaam_Kremar , Malibu_High , And_Give_Us_Our_Daily_Sex , Muqabala , Naukar , Bhayankara_rupa_se_dvarphsa , Alibaba_Aur_Chalis_Chor , Flying_High , American_Gigolo , Andher_Nagari , The_Blue_Lagoon , Caligula , Cruising , Dostana , Flash_Gordon , Aakhari_Yuddha , Insaaf_Ka_Tarazu , Saadhaaran_Log , Shaan , The_Shining , Superman_II , Thodisi_Bewafai , Body_Heat , Ek_Duje_Ke_Liye , The_Entity , Haathkadi , Laawaris , Private_Lessons , Raiders_of_the_Lost_Ark , Reds , Sharda , Southern_Comfort , Dhaariyon , Yarana , Yaraana , Basket_Case , Blade_Runner , Caligula_and_Messalina , Andhera_Kristal , Desh_Premi , the_Extra-Terrestrial , The_Evil_Dead , Gandhi , Aadimanav_Aur_Sarprani , Khuddar , A_Little_Sex , Kk_Adhikaaree_Aur_Ek_Jentalamain , Subah , Coolie , Door-Desh , Gehri_Chot , Jaane_Bhi_Do_Yaaro , The_King_of_Comedy , Meree_Krisamas,_Shree_Lorens , Bond_No_1 , Outsiders , Star_Wars:_Episode_VI_-_Return_of_the_Jedi , Scarface , Trading_Places , Woh_Saat_Din , Angel , Ghostbusters , Gremlins , Hollywood_Hot_Tubs , Indiana_Jones_and_the_Temple_of_Doom , Inquilab , Jaag_Utha_Insaan , Pavan_Kee_Ghaatee_Ka_Nausakhiya , Once_Upon_a_Time_in_America , Pet_Pyaar_Aur_Paap , Sixteen_Candles , The_Terminator , Dragon_Ball , Back_to_the_Future , The_Breakfast_Club , Faaslay , The_Goonies , Shaitani_Parbat , Khunkhar_Darinde , Pulis_Kee_Kahaanee , Roop_Ki_Rani_Jungle_Ka_Raja , Lavaa , Little_Flames , Saheb , A_View_to_A_Kill , Saakshee , Aliens , Allah-Rakha , Chopping_Mall , Eleven_Days_Eleven_Nights , Ferris_Buellers_Day_Off , The_Fly , Rahasyamayi_Balak , Jaanbaaz , Karma , Bhoolabhulaiya , The_Mosquito_Coast , Nagina , 9_Weeks , Gulaabee_Mein_Sundar , Stand_by_Me , Top_Gun , Welcome_to_18 , Kala_Naag , What_Every_Frenchwoman_Wants , Full_Metal_Jacket , Shaitan_Ka_Beta , The_Last_Emperor , The_Lost_Boys , Masques , Mr_India , Nayakan , Velu_Nayakan , Planes,_Trains_and_Automobile , Predator , Shahenshah , Jism_Ka_Sauda , The_Untouchables , Akira , Beetlejuice , Big_Business , Junglee_Jaanwar , Frantic , Grave_of_the_Fireflies , Inteqam , Cinema_Paradiso , Qayamat_Se_Qayamat_Tak , Rain_Man , Salaam_Bombay! , My_Neighbour_Totoro , Vijay , Legend_of_the_Galactic_Heroes , Appu_Raja , Batman , Chandni , Total_Rikol , Wild_Orchid , Backdraft , Benaam_Badsha , Cape_Fear , Dalpati_ , Dil_Hai_Ke_Manta_Nahin , Diwana_Mujhsa_Nahin , The_Marrying_Man , My_Girl , Only_Yesterday , Qurban , Robin_Hood , Saajan , Saudagar , The_Silence_of_the_Lambs , Terminator_2 , Basic_Instinct , Khatarnak_Chahat , Batman_Returns , Mrt_Mastishk , Dracula , All_Ladies_Do_It , Geet , Akela_Ghar_2 , Jeevan_Ek_Sunghursh , Jo_Jeeta_Wohi_Sikandar , Nishchay , he_Opposite_Sex_and_How_to_Live_with_Them , Reservoir_Dogs , Roja , Scent_of_a_Woman , Tirangaa , Tokyo_Decadence , Anmol , Baazigar , Bad_Boy_Bubby , Beyond_Bedlam , Indecent_Proposal , Jurassic_Park , Khal_Nayak , Naked , Prateeksha , Jail_Ki_Chidiya , Roop_Ki_Rani_Choron_Ka_Raja , Schindler's_List , Sliver , Suraj_Ka_Satvan_Ghoda , Chor_Chor , Friends , Babys_Day_Out , Bandit_Queen , Phoolan_Devi , Darr , Cold_Water , Eena_Meena_Deeka , Forrest_Gump , Hum_Aapke_Hain_Koun , HAHK , The_Lion_King , The_Professional , Parmatma , Pulp_Fiction , Kam_Gaharee_Kabr , The_Shawshank_Redemption , The_Smile_of_the_Fox , Swaram , True_Lies , Katil_Ki_Khoj , Aao_Pyaar_Karen , Ab_Insaaf_Hoga , Apollo_13 , Bad_Boys , Braveheart , Awwal_Number , Bombay_Ki_Sair , Baradari , Chor_Bazaar , Daksha_Yagna , Following , Heer_Sial , Joydev , Kabuli_Khan , Blackmail , Kala_Dhandha , Khilauna , Mem_Sahib , Pataal_Bhairavi , Chacha_Charlie , Sau_Karod , Swarg_Se_Sunder , Thief_of_Tartar , Vair_Ka_Badla , Daasi , Bombay_Ki_Mohini , Delhi_Durbar , Nagan_Ki_Ragini , Kathodu_Kathoram , Mahachor , Jawaharlal_Nehru , Pandit_Nehru , Main_Hoon_Hindustani , Purnima , Ranee , Redrose , Mohabbat_Ki_Kasauti , Shri_Ram_Hanuman_Yuddha , Vamsa_Vriksh , Aparadhi_Abla , Balak_Aur_Janwar , Chaitanya_Mahaprabhu , Bhagaban_Shrikrishna_Chaitanya , Paraya_Dhan , Raj_Nartaki , Daal_Mein_Kala , Daku , Daku_Manzoor , Ek_Chidiya_Anek_Chidiya , Hariyali_Aur_Raasta , Heera_Aur_Patthar , How_They_Make_Adult_Movies , Inteqam , Joru_Ka_Ghulam , Dayasagar , Daya_Sagar , Kaash , Kumkum_the_Dancer , Lat_Sahib , Mabap_Ki_Laj , Naag_Rani , Milan , Pyase_Panchhi , Radha_Madhav , Lal_Vavto , Sunhera_Sansar , Shubha_Lagna , Tumhaare_Bina , Ankush , Chit_Chor , Dreamgirl , Chhota_Bhai , Safed_Jhooth , Seshpath , Shiv_Parvati , Sheesha , Brijs_Taqdeer , Tumse_Achcha_Kaun_Hai , Mahabharata , Awam , Qurbani , Nikah , Pati_Patni_Aur_Woh , Oonch_Neech , Sholay , Tumhari_Kasam , Sex_and_the_City , The_Wood , Cast_Away , American_Pie , Chhote_Miyaan , Ankhiyon_Ke_Jharokhon_Se , The_Lord_of_the_Rings , The_Sixth_Sense , Boredom , Lagaan , American_Beauty , The_White_Ship , Bombay_Ka_Babu , Chaahat , Vijeta , Zehreelay , Karz_Chukana_Hai , Kuch_Kuch_Hota_Hai , KKHH , Pyar_Kiya_To_Darna_Kya , Pyar_To_Hona_Hi_Tha , Siska , Frivolous_Lola , Dhadkan , Do_Dil , Gehra_Daagh , Golden_Eyes_Secret_Agent_077 , Rustam_Kuan , Tarzan_Delhi_Mein , The_Danger_Girls , Aaj_Ki_Taaza_Khabar , Aakhri_Dao , Nischay , Asha , Aashiana , Ek_Mausam_Chhota_Sa , Aasman , Abhi_To , Aarohi , Requiem_for_a_Dream , Little_Nicky , Aakhri_Sangram , Dharam_Adhikari , Hairaan , Johny_Ustad , Mrs_Malini_Iyer , Nigahen , Patthar_Ke_Insaan , Chandramukhi_Devdas , Chandramukhi_Devdaas , Raampur_Ka_Raja , Romance , Schoolgirls_in_Chains , Bionic_Ninja , Saat_Nanhe_Karate_Ustaad , Gandhi_Se_Mahatma_Tak , Wolf_Guy , Sexy , Sexy_Beast , Paths_in_the_Night , Naked_Video , Yeh_Pyaar_Hi_To_Hai , Sambandh , Jawan_Mohabbat , Kachche_Dhaage , Hindustan_Ki_Kasam , Snatch , Memento , Italian_Kamasutra , Amelie , Aashiana , Dhyanu_Bhakt , Oggy_and_the_Cockroaches , Aatish_e_Ishq , Bhagyavaan , Bhul_Bhulaiyan , Budtameez , Bulbul_E_Paristan , Dharam_Veer , Poladi_Pahelwan , Inteqam , Jawahir_e_Hind , Qismat , Lal_Cheetah , Malena , Malena , Mohabbatein , Gul_e_Bakawali , Raampur_Ka_Lakshman , Madan_Mohana , Shadi , Sipah_Salar , Surya_Kumari , Suryavansham , Swarajyacha_Toran , Vichitra_Ver , Buddhibal , Dragon_Ball_Z , Bhisti , Bachha_I_Sakka , Dehati_Ladki , Do_Auratein , Ghulam , Ghulam_Daku , Kishen_Kanhaiya , Swarnalata , Yamla_Jatt , Shri_Radha_Krishna , Byalis , Achanak , Baraat , Dashavatar , Kashti , Khandaani , Minaar , Dawedaar , Pratigya , Hum_Saath_aath_Hain , Atoot , Pukar , Original_Sin , Hum_Tumhare_Hain_Sanam , 1_2_Ka_4 , Bharati , Barf_Ka_Toofan , Bombay_Ki_Billi , Ek_Kali_Muskayee , Jaanwar , Ek_Aur_Atyachar , Khabardar , Khubsoorat , Rivaj , Shri_Vatsa , Sipah_Salar , Andheri_Raat_Mein_Diya_Tere_Haath_Mein , Baap_Re_Baap , Badi_Bahen , Badnaam , Awara_Raqasa , 24_Ghante , Darasingh , Dil_E_Nadaan , Dil_Ruba , Ghar_Ghar_Ki_Kahani , Virni_Vibhuti , Hum_Sab_Chor_Hain , Sabz_Pari , Jeene_Nahin_Doonga , Kappa_Bilupu , Dushman_Ni_Dikri , Malammanna_Pavada , Mela , Milap , Pavitra_Satan , Devi_Ya_Danvi , Zulmi_Kansa , Sapno_Ka_Suadagar , Sati_Ka_Shaap , Shareef_Badmash , Vichithra_Duniya , Ameer_Garib , Amrit , Angaarey , Anokha_Bandhan , Shiv_Bhakt_Siriyala , Bindiya , Chikni_Chachi , Deivapiravi , Dhadakebaaz , Door_Ka_Rahi , Engal_Thangam , Hello_Brother , Phir_Janam_Lenge_Hum , Kaho_Naa_Pyaar_Hai , KNPH , Kranti , Love_Sex , Marte_Dam_Tak , Meet_Mere_Mann_Ke , Na_Insaafi , Noorjehan , Abhaas , Talaash_e_Haq , Talaash_e_Haq , Shoor_Veer , Pyas , Faraar , Sonano_Suraj , Ek_Anaar_Sau_Bimaar , Gaddar , Devdas , Navi_Sethani , Diler_Daring , Haseena_Maan_Jaayegi , Sacho_Haqdaar , Hridaya_Triputi , Parijatak , Ahmedabad_Ni_Sethani , Adarsha_Veerangana , Do_Dhari_Talwar , Hairee_Pautar_aur_Paaras_Patthar , Jalim_Jawani , Chandraprabha , Sabur_Shah , Naharsinh_Daku , Nur_Jehan , Anjaan_Hai_Koi , Hera_Pheri , Judai_Shatranji , The_Matrix_Revolutions , Saat_Sawal , Samay_Ki_Dhara , Bombay_Ka_Maharaja , Khoon_Ki_Qeemat , Farz_Aur_Mohabbat , Nausherwan_E_Adil , Sambandh , Chal_Chal_Re_Naujawan , Keechaka_Vadham , Shiv_Leela , Rukmini_Satyabhama , Buddha_Mil_Gaya , Police_ki_jung , Khoobsurat , Sirf_Tum , Spirited_Away , Aur_Tumhaaree_Maan_Bhee , Shin_Chan , Alluda_Mazaaka , Mera_Maqsad , Donga , Qeemat , Khiladi_No_1 , Dharti_Ki_Kasam , Trinetra_The_Third_Eye , Main_Hoon_Rakhwala , Police_Inspector , Farrar_Qaidi , Wardat , Amanush , Behan_Ka_Prem , Inteqam , Kora_Kaghaz , Sharat_Sandhya , Naiya , Saraswati_lakshmi_parvati , Devi_Saraswati , Shree_Krishna_Leela , Shiv_Kripa , Bhakt_Prahlad , Qismatwala , AMALL , Anth , Anadi_Khiladi , Dulhan_Hum_Le_Jayenge , Kaamchor , Kabhi_Khushi_Kabhie_Gham , KKKG , K3G , Pehli_Tareekh , Samrat_Hamir , Savitri_Satyavan , Surekha_Abhimanyu , Dil_Tera_Deewana , Do_Kaliyaan , Joroo_Ka_Ghulam , Killing_Me_Softly , Prem_Pujari , Unfaithful , Amar_shaheed , KBC , Shri_Rachhodrai , Gunda_Gardi , Streeyaraj , Mayor_Sahab , Insaaf , Shreshthata_Ki_Vidya , Vidya_Haran , Mahaanta , Shap_Sambhram , Chand_Ka_Tukda , Pehechaan , Pehchan , Police_Aur_Mujrim , Pushpak , Samantak_Mani , Jagdev_Parmar , Shapath , Shiva_Mahima , Bali_Raja , Krishna_Bhakta_Sudama , Daivi_Khajina , Diler_Jigar , Heist , Kanyasulkam , Bhakta_Prahlad , Janaki_Swayamwara , Sati_Mahananda , Municipal_Nivadnuk , The_Pianist , Bhakta_Shiromani , Prabhu_Jai_Shri_Ram , Sanlagna_Ras , Vachambang , Vinchavacha_Dansha , Ganga_Bhawani , Sex_and_Lucia , Koi_Mil_Gaya , Ram_Doota , Sati_Renuka , Parsuram_Avtar , Fauladi_Jigar , Vasantha_Maligai , Bhagyavati , Desh_Ke_Gaddar , Jay_Vijay , Kalyug_Ki_Sati , Kalaa_Paani , Saza_E_Kala_Pani , Manohar , Manohar , Intimacy , Khatarnak_Khel , Sati_Ansuya , Mann_Ka_Meet , Savitri , Bhagwan_Balaji , Road_to_Perdition , Akhiri_Intaqam , Narasinh_Avatar , Kamyab , Mera_Farz , Ayodhya_Ka_Raja , Jamai_Babu , En_Thangai_Kalyani , Ladki , Triya_Rajya , Ramayana , Rangeen_Duniya , Insaaf_Ki_Pukar , Maang_Bharo_Sajana , Purani_Haveli , Purana_Mandir_2 , Saamri , Veerana , Durga_Mata , Bhakti_Mahima , The_Pornographer , Husn_Ka_Ghulam , Rajrani_Mira , Zor , Catch_Me_If_You_Can , Ghar_Ki_Laxmi , Kuldipak , Misserka_Khazana , The_Girl_Next_Door , Shuk_Rambha , Barrister_Ki_Bibi , Battle_Royale , Biwi_O_Biwi , Khatarnak_Khiladi , Nimo_dhumdhana , Hollywood_Sex_Fantasy , Kill_Bill , H_S_Rawails_Mere_Mehboob , Sagai , Shagoofa , Vijaykumar , Zidd , Asra , Aatish_Feel_the_Fire , Black_Angel , Bismil_Ki_Aarzoo , Haseena_Maan_Jayegi , Hasina_Maan_Jayegi , Papi_Gudia , Jab_Jab_Pyaar_Hua , Ramayana , Ajnabee , Anand_Ashram , Lalkar , Phir_Subah_Hogi , Angaarey , A_Beautiful_Mind , Chhum_Chhama_Chhum , Jeevan_Jyoti , Raja_Ki_Ayegi_Baraat , Bewafa_Ashq , Daku_Hasina , Dr_Babasaheb_Ambedkar , Kab_Kyon_Aur_Kahan , Daagh_The_Fire , Rasila_Premi , Mujhse_Dosti_Karoge! , Do_Hazaar_Ek , Gul_Bakavali , Mehndi , Narasimham , Policewala_Gunda , tamasha , panipath , hathi_mere_sathi , ramleela , war , student_of_the_year , shadi_me_jaroor_ana , yariyaan , namaste_londan , baggi , kahani , manat , bajarangi_bhaijaan , race , kick , wanted , prem_ratan_dhan_payo , my_name_is_khan , jab_tak_hai_jaan , kedarnath , dil_bechara , chhichhore , love_aaj_kal , ajab_pem_ki_gajab_kahani , pk , dangal , secret_superstar , makkhi , suryavansham , dhishoom , muder , jism , wajah_tum_ho , rais , section_375 , pink , kill_dill , raja_babu , tanhaji , padmavat , singam , sub_mangal_savdhan , gulabo ,shoot_out_at_vadala , dhamal , golmaal , angregi_mediam , bagbaan , badsha , bang_bang , malang , kalank , gangajal , sonu_ke_titu_ki_sweety , chenai_express , raone , 3_idiots , krish , raees , om_santi_om , don , agneepath , kabir_shing , bhootnath , fanaa , bajirao_mastani , dilwale , ramaiya_vastavaiya , bolbachan , devdas , prem_leela , chak_de_india , aamdani_athani_kharcha_rupaiyaa , bahubali , takdeer , blackmail ,flying_jatt , good_news , dhadak , kal_ho_na_ho , khiladi_786 , raazi , m_s_dhoni , haider , sanju , sholay , new_york , super30 , agent_vinod , kesari , talash , tiger , tare_jamin_par , vivah , himatvala , chhelo_divash , su_thayu ,"     
global ch
ch="a"



class MainWindow(Screen):
    username:ObjectProperty(None)
    score : NumericProperty(0)
    
    def add_user(self):
        con = sql.connect('user.list')
        cur = con.cursor()
        global globusername
        global prevscore
        globusername = self.username.text
        try:
            cur.execute("""SELECT score FROM username WHERE user = ? """,(self.username.text,))
            data = cur.fetchall()
            self.score = data[0][0]
            print(self.score)
            
            con.commit()
        except:
            print("user is not availabel")
            self.score = 0
        
        prevscore = self.score
        cur.execute("""INSERT INTO username VALUES(?,?)""",(self.username.text,self.score))
        con.commit()
        
        
        
        con.close()
class GameWindow(Screen):
    userinput = ObjectProperty(None)
    chatarea = ObjectProperty(None)
    score = ObjectProperty(None)
    ch = StringProperty("a")
    def changetomain(self):
        App.get_running_app().stop()
        print ("close pressd")
    def exit(self):
        layout = GridLayout(cols = 1, padding = 10)
        popupLabel = Label(text ="you wanna exit ? ")
        popupyesButton = Button(text = "YES")
        popupnoButton = Button(text = "NO")
        layout.add_widget(popupLabel)
        layout.add_widget(popupyesButton)
        layout.add_widget(popupnoButton)
        popup = Popup(title ='tusi ja rahe ho ??', 
                  content = layout)   
        popupnoButton.bind(on_press = popup.dismiss)
        popupyesButton.bind(on_press = lambda x :self.changetomain())
        popup.open()

    def sendclk(self):
        global ch
        global movielist
        global prevscore
        if(self.userinput.text.startswith(ch) or self.userinput.text.startswith(ch.upper())):
            confirm=True
        else:
            confirm=False
            layout = GridLayout(cols = 1, padding = 10)
            popupLabel = Label(text = "Opps! You enter the wrong ...\n You lose\nYour score is : "+self.score.text)
            layout.add_widget(popupLabel)
            popup = Popup(title ='Better luck next time', 
                      content = layout)   
            popup.open()
            if(prevscore < int(self.score.text)):

                con = sql.connect('user.list')
                cur = con.cursor()
                cur.execute("""UPDATE username SET score = ? WHERE user = ? """,(int(self.score.text),globusername) )
                con.commit()
        
        confirm =bool(re.search(r'\b'+self.userinput.text+r'\b',movielist,re.IGNORECASE))
        if(confirm):
            #user side
            tempstr = self.chatarea.text
            tempstr = tempstr + "\n" +"user : "+self.userinput.text
            self.chatarea.text = tempstr
            movielist = re.sub(r'\b'+self.userinput.text+r'\b',",",movielist,flags=re.IGNORECASE)
            ch=self.userinput.text[len(self.userinput.text)-1]
            self.userinput.text = ""
            
            scoreint = int(self.score.text)
            scoreint = scoreint + 1 
            self.score.text = str(scoreint)
            movielist =re.sub(", ,",",",movielist)
            movielist =re.sub(", ,",",",movielist)
            

            #cpu side
            f_ch_s=re.search(r"\b"+ch+"+",movielist,re.IGNORECASE)
            if (f_ch_s== None):
                layout = GridLayout(cols = 1, padding = 10)
                popupLabel = Label(text = "Opps! You win this game ...\n You lose\nYour score is : infinity ")
                layout.add_widget(popupLabel)
                popup = Popup(title ='you are osm ', 
                          content = layout)   
                popup.open()
                if(prevscore < int(self.score.text)):

                    con = sql.connect('user.list')
                    cur = con.cursor()
                    cur.execute("""UPDATE username SET score = ? WHERE user = ? """,(int(self.score.text),globusername) )
                    con.commit()
            i=f_ch_s.start()
            test_str=movielist[i]
            cpu_word =""
            while (test_str != " "):
                test_str=movielist[i]
                cpu_word = cpu_word+test_str
                i=i+1
            tempstr = self.chatarea.text
            tempstr = tempstr + "\n" +"cpu  : "+cpu_word
            self.chatarea.text = tempstr
            ch=cpu_word[len(cpu_word)-2]
            movielist = re.sub(r'\b'+cpu_word+r'\b',",",movielist,flags=re.IGNORECASE)
            movielist =re.sub(", ,",",",movielist)
            movielist =re.sub(", ,",",",movielist)

        else:
            layout = GridLayout(cols = 1, padding = 10)
            popupLabel = Label(text = "Opps! You enter the wrong ...\n You lose\nYour score is : "+self.score.text)
            layout.add_widget(popupLabel)
            popup = Popup(title ='Better luck next time', 
                      content = layout)   
            popup.open()
            if(prevscore < int(self.score.text)):


                con = sql.connect('user.list')
                cur = con.cursor()
                cur.execute("""UPDATE username SET score = ? WHERE user = ? """,(int(self.score.text),globusername) )
                con.commit()


class RuleWindow(Screen):
    pass

class ScoreWindow(Screen):
    labsc=ObjectProperty(None)
    def __init__(self, **kwargs):
        super(ScoreWindow,self).__init__(**kwargs)
        con = sql.connect('user.list')
        cur = con.cursor()
        cur.execute("""SELECT * FROM username ORDER BY score DESC """)
        allscr = cur.fetchall()
        con.commit()
        global scorelist
        scorelist = ""
        for i in allscr:
            spc = 15-len(i[0])
            scorelist = scorelist + "\nusername : "+i[0]+" "*spc+"score: "+str(i[1])

        print("this is scorelist\n")
        print(scorelist)
        print("here scorelist over\n")
    def press(self):
        global scorelist
        print("pressed")
        self.labsc.text = scorelist

      

        
        


class WindowManager(ScreenManager):
    pass




    
            
    
kv = Builder.load_file("start.kv")    
    

class startgame(App):
    def build(self):
        movielist="Sadhu_Aur_Shaitaan , Rain_or_Shine , Platinum_Blonde , Shopworn , The_Story_of_Temple_Drake , Jeevan_Naiya , Modern_Times , Sabotage , Second_Chorus , Aarzoo , Prelude_to_War , National_Velvet , Phool , Rattan , Udahir_Path , Conflict , The_Ghost_Lady , Shahjehan , Dil_Ki_Rani , Good_News , Road_to_Rio , Port_of_Call , Red_River , Scott_of_the_Antarctic , Aarzoo , Dastaan , Khilari , Rashomon , Awara , Bahar , Daagh , Road_to_Bali , Aah , Paapi , Black_Widow , Boot_Polish , Ilzaam , Naukri , Seven_Samurai , Ghar_Number_44 , Shri_420 , Udaan_Khatola , Udan_Khatola , Delhi_Mein , Anjaan , Somewhere_in_Delhi , Chhoo_Mantar , Ek_Hi_Raasta , Kismat_Ka_Khel , Qismat_Ka_Khel , 12_Angry_Men , Bharat_Mata , Kathputli , Witness_for_the_Prosecution , Kala_Pani , Hiroshima_Mon_Amour , Insaan_Jaag_Utha , Main_Nashey_Mein_Hoon , Rio_Bravo , Bambai_Ka_Babu , Bombay_Ka_Babu , Barsat_ki_Rat , Dil_Apna_Aur_Preet_Parai , Kaala_Bazaar , The_Thief_of_Baghdad , Psycho , Ganga_Jamuna , Mem_Didi , Mutiny_on_the_Bounty , Sanjuro , Tarzan_Meera_Saathi , Gharbar , Yeh_Raaste_Hain_Pyar_Ke , Ishara , Blood_and_Black_Lace , Woman_in_the_Dunes , Aarzoo , Chemmeen_Lahren , Kapurush_Mahapurush , Khandaan , The_Good_the_Bad_and_the_Ugly , Dil_Diya_Dard_Liya , Chelsea_Girls , Chhoti_Si_Mulaqaat , Humraaz , The_Nude_Restaurant , Point_Blank , Anjam , The_Bliss_of_Mrs._Blossom , Blue_Movie , Bombay_Raat_Ki_Bahon_Mein , Deewana , Enter_the_Game_of_Death , Sangharsh , Sunghursh , Sungharsh , Gali_Gali_Sim_Sim , Marlowe , Pyar_Hi_Pyar , A_Thousand_&_One_Nights , Talaash , The_Love_Factor , Days_and_Nights_in_the_Forest , The_Great_White_Hope , Hollywood_Blue , Ilzaam , Ryans_Daughter , Anand , Kolkata_71 , Karwan , Sharmilee , Murmur_of_the_Heart , Bawarchi , The_Godfather , Sweet_Sugar , Doraemon , Distant_Thunder , Enter_the_Dragon , The_Exorcist , Shaitaanee_Raat , Malicious , Mann_Jeete_Jag_Jeet , Namak_Haram , Zanjeer , Belladonna_of_Sadness , Bruce_Li_Ka_Inteqaam , Chhattis_Ghante , Geeta_Mera_Naam , The_Godfather , The_Holy_Mountain , The_Night_Porter , Deewar , The_Story_of_O , Jaws , One_Flew_Over_the_Cuckoos_Nest , Sholay , Kranti_Ki_Tarangein , Zakhmi , Paris_Ki_Ek_Shyam , Jackson_County_Jail , Taxi_Driver , Bhumika , Teesaree_Prakaar_Kee_Muthabhed , Hum_Kisi_Se_Kum_Nahin , Imaan_Dharam , Saturday_Night_Fever , Submission , Shatranj_Ke_Khiladi , Playing_with_Love , Star_Wars , Empire_of_Passion , Athithi , Badalte_Rishte , Blue_Movie , Don , International_Velvet , Midnight_Express , Satyam_Shivam_Sundaram , Sita_Aur_Gita , Trishul , Ehsaas , Alien , Amardeep , Apocalypse_Now , American_Dragula , Hasino_Ka_Kabila , Kremar_Banaam_Kremar , Malibu_High , And_Give_Us_Our_Daily_Sex , Muqabala , Naukar , Bhayankara_rupa_se_dvarphsa , Alibaba_Aur_Chalis_Chor , Flying_High , American_Gigolo , Andher_Nagari , The_Blue_Lagoon , Caligula , Cruising , Dostana , Flash_Gordon , Aakhari_Yuddha , Insaaf_Ka_Tarazu , Saadhaaran_Log , Shaan , The_Shining , Superman_II , Thodisi_Bewafai , Body_Heat , Ek_Duje_Ke_Liye , The_Entity , Haathkadi , Laawaris , Private_Lessons , Raiders_of_the_Lost_Ark , Reds , Sharda , Southern_Comfort , Dhaariyon , Yarana , Yaraana , Basket_Case , Blade_Runner , Caligula_and_Messalina , Andhera_Kristal , Desh_Premi , the_Extra-Terrestrial , The_Evil_Dead , Gandhi , Aadimanav_Aur_Sarprani , Khuddar , A_Little_Sex , Kk_Adhikaaree_Aur_Ek_Jentalamain , Subah , Coolie , Door-Desh , Gehri_Chot , Jaane_Bhi_Do_Yaaro , The_King_of_Comedy , Meree_Krisamas,_Shree_Lorens , Bond_No_1 , Outsiders , Star_Wars:_Episode_VI_-_Return_of_the_Jedi , Scarface , Trading_Places , Woh_Saat_Din , Angel , Ghostbusters , Gremlins , Hollywood_Hot_Tubs , Indiana_Jones_and_the_Temple_of_Doom , Inquilab , Jaag_Utha_Insaan , Pavan_Kee_Ghaatee_Ka_Nausakhiya , Once_Upon_a_Time_in_America , Pet_Pyaar_Aur_Paap , Sixteen_Candles , The_Terminator , Dragon_Ball , Back_to_the_Future , The_Breakfast_Club , Faaslay , The_Goonies , Shaitani_Parbat , Khunkhar_Darinde , Pulis_Kee_Kahaanee , Roop_Ki_Rani_Jungle_Ka_Raja , Lavaa , Little_Flames , Saheb , A_View_to_A_Kill , Saakshee , Aliens , Allah-Rakha , Chopping_Mall , Eleven_Days_Eleven_Nights , Ferris_Buellers_Day_Off , The_Fly , Rahasyamayi_Balak , Jaanbaaz , Karma , Bhoolabhulaiya , The_Mosquito_Coast , Nagina , 9_Weeks , Gulaabee_Mein_Sundar , Stand_by_Me , Top_Gun , Welcome_to_18 , Kala_Naag , What_Every_Frenchwoman_Wants , Full_Metal_Jacket , Shaitan_Ka_Beta , The_Last_Emperor , The_Lost_Boys , Masques , Mr_India , Nayakan , Velu_Nayakan , Planes,_Trains_and_Automobile , Predator , Shahenshah , Jism_Ka_Sauda , The_Untouchables , Akira , Beetlejuice , Big_Business , Junglee_Jaanwar , Frantic , Grave_of_the_Fireflies , Inteqam , Cinema_Paradiso , Qayamat_Se_Qayamat_Tak , Rain_Man , Salaam_Bombay! , My_Neighbour_Totoro , Vijay , Legend_of_the_Galactic_Heroes , Appu_Raja , Batman , Chandni , Total_Rikol , Wild_Orchid , Backdraft , Benaam_Badsha , Cape_Fear , Dalpati_ , Dil_Hai_Ke_Manta_Nahin , Diwana_Mujhsa_Nahin , The_Marrying_Man , My_Girl , Only_Yesterday , Qurban , Robin_Hood , Saajan , Saudagar , The_Silence_of_the_Lambs , Terminator_2 , Basic_Instinct , Khatarnak_Chahat , Batman_Returns , Mrt_Mastishk , Dracula , All_Ladies_Do_It , Geet , Akela_Ghar_2 , Jeevan_Ek_Sunghursh , Jo_Jeeta_Wohi_Sikandar , Nishchay , he_Opposite_Sex_and_How_to_Live_with_Them , Reservoir_Dogs , Roja , Scent_of_a_Woman , Tirangaa , Tokyo_Decadence , Anmol , Baazigar , Bad_Boy_Bubby , Beyond_Bedlam , Indecent_Proposal , Jurassic_Park , Khal_Nayak , Naked , Prateeksha , Jail_Ki_Chidiya , Roop_Ki_Rani_Choron_Ka_Raja , Schindler's_List , Sliver , Suraj_Ka_Satvan_Ghoda , Chor_Chor , Friends , Babys_Day_Out , Bandit_Queen , Phoolan_Devi , Darr , Cold_Water , Eena_Meena_Deeka , Forrest_Gump , Hum_Aapke_Hain_Koun , HAHK , The_Lion_King , The_Professional , Parmatma , Pulp_Fiction , Kam_Gaharee_Kabr , The_Shawshank_Redemption , The_Smile_of_the_Fox , Swaram , True_Lies , Katil_Ki_Khoj , Aao_Pyaar_Karen , Ab_Insaaf_Hoga , Apollo_13 , Bad_Boys , Braveheart , Awwal_Number , Bombay_Ki_Sair , Baradari , Chor_Bazaar , Daksha_Yagna , Following , Heer_Sial , Joydev , Kabuli_Khan , Blackmail , Kala_Dhandha , Khilauna , Mem_Sahib , Pataal_Bhairavi , Chacha_Charlie , Sau_Karod , Swarg_Se_Sunder , Thief_of_Tartar , Vair_Ka_Badla , Daasi , Bombay_Ki_Mohini , Delhi_Durbar , Nagan_Ki_Ragini , Kathodu_Kathoram , Mahachor , Jawaharlal_Nehru , Pandit_Nehru , Main_Hoon_Hindustani , Purnima , Ranee , Redrose , Mohabbat_Ki_Kasauti , Shri_Ram_Hanuman_Yuddha , Vamsa_Vriksh , Aparadhi_Abla , Balak_Aur_Janwar , Chaitanya_Mahaprabhu , Bhagaban_Shrikrishna_Chaitanya , Paraya_Dhan , Raj_Nartaki , Daal_Mein_Kala , Daku , Daku_Manzoor , Ek_Chidiya_Anek_Chidiya , Hariyali_Aur_Raasta , Heera_Aur_Patthar , How_They_Make_Adult_Movies , Inteqam , Joru_Ka_Ghulam , Dayasagar , Daya_Sagar , Kaash , Kumkum_the_Dancer , Lat_Sahib , Mabap_Ki_Laj , Naag_Rani , Milan , Pyase_Panchhi , Radha_Madhav , Lal_Vavto , Sunhera_Sansar , Shubha_Lagna , Tumhaare_Bina , Ankush , Chit_Chor , Dreamgirl , Chhota_Bhai , Safed_Jhooth , Seshpath , Shiv_Parvati , Sheesha , Brijs_Taqdeer , Tumse_Achcha_Kaun_Hai , Mahabharata , Awam , Qurbani , Nikah , Pati_Patni_Aur_Woh , Oonch_Neech , Sholay , Tumhari_Kasam , Sex_and_the_City , The_Wood , Cast_Away , American_Pie , Chhote_Miyaan , Ankhiyon_Ke_Jharokhon_Se , The_Lord_of_the_Rings , The_Sixth_Sense , Boredom , Lagaan , American_Beauty , The_White_Ship , Bombay_Ka_Babu , Chaahat , Vijeta , Zehreelay , Karz_Chukana_Hai , Kuch_Kuch_Hota_Hai , KKHH , Pyar_Kiya_To_Darna_Kya , Pyar_To_Hona_Hi_Tha , Siska , Frivolous_Lola , Dhadkan , Do_Dil , Gehra_Daagh , Golden_Eyes_Secret_Agent_077 , Rustam_Kuan , Tarzan_Delhi_Mein , The_Danger_Girls , Aaj_Ki_Taaza_Khabar , Aakhri_Dao , Nischay , Asha , Aashiana , Ek_Mausam_Chhota_Sa , Aasman , Abhi_To , Aarohi , Requiem_for_a_Dream , Little_Nicky , Aakhri_Sangram , Dharam_Adhikari , Hairaan , Johny_Ustad , Mrs_Malini_Iyer , Nigahen , Patthar_Ke_Insaan , Chandramukhi_Devdas , Chandramukhi_Devdaas , Raampur_Ka_Raja , Romance , Schoolgirls_in_Chains , Bionic_Ninja , Saat_Nanhe_Karate_Ustaad , Gandhi_Se_Mahatma_Tak , Wolf_Guy , Sexy , Sexy_Beast , Paths_in_the_Night , Naked_Video , Yeh_Pyaar_Hi_To_Hai , Sambandh , Jawan_Mohabbat , Kachche_Dhaage , Hindustan_Ki_Kasam , Snatch , Memento , Italian_Kamasutra , Amelie , Aashiana , Dhyanu_Bhakt , Oggy_and_the_Cockroaches , Aatish_e_Ishq , Bhagyavaan , Bhul_Bhulaiyan , Budtameez , Bulbul_E_Paristan , Dharam_Veer , Poladi_Pahelwan , Inteqam , Jawahir_e_Hind , Qismat , Lal_Cheetah , Malena , Malena , Mohabbatein , Gul_e_Bakawali , Raampur_Ka_Lakshman , Madan_Mohana , Shadi , Sipah_Salar , Surya_Kumari , Suryavansham , Swarajyacha_Toran , Vichitra_Ver , Buddhibal , Dragon_Ball_Z , Bhisti , Bachha_I_Sakka , Dehati_Ladki , Do_Auratein , Ghulam , Ghulam_Daku , Kishen_Kanhaiya , Swarnalata , Yamla_Jatt , Shri_Radha_Krishna , Byalis , Achanak , Baraat , Dashavatar , Kashti , Khandaani , Minaar , Dawedaar , Pratigya , Hum_Saath_aath_Hain , Atoot , Pukar , Original_Sin , Hum_Tumhare_Hain_Sanam , 1_2_Ka_4 , Bharati , Barf_Ka_Toofan , Bombay_Ki_Billi , Ek_Kali_Muskayee , Jaanwar , Ek_Aur_Atyachar , Khabardar , Khubsoorat , Rivaj , Shri_Vatsa , Sipah_Salar , Andheri_Raat_Mein_Diya_Tere_Haath_Mein , Baap_Re_Baap , Badi_Bahen , Badnaam , Awara_Raqasa , 24_Ghante , Darasingh , Dil_E_Nadaan , Dil_Ruba , Ghar_Ghar_Ki_Kahani , Virni_Vibhuti , Hum_Sab_Chor_Hain , Sabz_Pari , Jeene_Nahin_Doonga , Kappa_Bilupu , Dushman_Ni_Dikri , Malammanna_Pavada , Mela , Milap , Pavitra_Satan , Devi_Ya_Danvi , Zulmi_Kansa , Sapno_Ka_Suadagar , Sati_Ka_Shaap , Shareef_Badmash , Vichithra_Duniya , Ameer_Garib , Amrit , Angaarey , Anokha_Bandhan , Shiv_Bhakt_Siriyala , Bindiya , Chikni_Chachi , Deivapiravi , Dhadakebaaz , Door_Ka_Rahi , Engal_Thangam , Hello_Brother , Phir_Janam_Lenge_Hum , Kaho_Naa_Pyaar_Hai , KNPH , Kranti , Love_Sex , Marte_Dam_Tak , Meet_Mere_Mann_Ke , Na_Insaafi , Noorjehan , Abhaas , Talaash_e_Haq , Talaash_e_Haq , Shoor_Veer , Pyas , Faraar , Sonano_Suraj , Ek_Anaar_Sau_Bimaar , Gaddar , Devdas , Navi_Sethani , Diler_Daring , Haseena_Maan_Jaayegi , Sacho_Haqdaar , Hridaya_Triputi , Parijatak , Ahmedabad_Ni_Sethani , Adarsha_Veerangana , Do_Dhari_Talwar , Hairee_Pautar_aur_Paaras_Patthar , Jalim_Jawani , Chandraprabha , Sabur_Shah , Naharsinh_Daku , Nur_Jehan , Anjaan_Hai_Koi , Hera_Pheri , Judai_Shatranji , The_Matrix_Revolutions , Saat_Sawal , Samay_Ki_Dhara , Bombay_Ka_Maharaja , Khoon_Ki_Qeemat , Farz_Aur_Mohabbat , Nausherwan_E_Adil , Sambandh , Chal_Chal_Re_Naujawan , Keechaka_Vadham , Shiv_Leela , Rukmini_Satyabhama , Buddha_Mil_Gaya , Police_ki_jung , Khoobsurat , Sirf_Tum , Spirited_Away , Aur_Tumhaaree_Maan_Bhee , Shin_Chan , Alluda_Mazaaka , Mera_Maqsad , Donga , Qeemat , Khiladi_No_1 , Dharti_Ki_Kasam , Trinetra_The_Third_Eye , Main_Hoon_Rakhwala , Police_Inspector , Farrar_Qaidi , Wardat , Amanush , Behan_Ka_Prem , Inteqam , Kora_Kaghaz , Sharat_Sandhya , Naiya , Saraswati_lakshmi_parvati , Devi_Saraswati , Shree_Krishna_Leela , Shiv_Kripa , Bhakt_Prahlad , Qismatwala , AMALL , Anth , Anadi_Khiladi , Dulhan_Hum_Le_Jayenge , Kaamchor , Kabhi_Khushi_Kabhie_Gham , KKKG , K3G , Pehli_Tareekh , Samrat_Hamir , Savitri_Satyavan , Surekha_Abhimanyu , Dil_Tera_Deewana , Do_Kaliyaan , Joroo_Ka_Ghulam , Killing_Me_Softly , Prem_Pujari , Unfaithful , Amar_shaheed , KBC , Shri_Rachhodrai , Gunda_Gardi , Streeyaraj , Mayor_Sahab , Insaaf , Shreshthata_Ki_Vidya , Vidya_Haran , Mahaanta , Shap_Sambhram , Chand_Ka_Tukda , Pehechaan , Pehchan , Police_Aur_Mujrim , Pushpak , Samantak_Mani , Jagdev_Parmar , Shapath , Shiva_Mahima , Bali_Raja , Krishna_Bhakta_Sudama , Daivi_Khajina , Diler_Jigar , Heist , Kanyasulkam , Bhakta_Prahlad , Janaki_Swayamwara , Sati_Mahananda , Municipal_Nivadnuk , The_Pianist , Bhakta_Shiromani , Prabhu_Jai_Shri_Ram , Sanlagna_Ras , Vachambang , Vinchavacha_Dansha , Ganga_Bhawani , Sex_and_Lucia , Koi_Mil_Gaya , Ram_Doota , Sati_Renuka , Parsuram_Avtar , Fauladi_Jigar , Vasantha_Maligai , Bhagyavati , Desh_Ke_Gaddar , Jay_Vijay , Kalyug_Ki_Sati , Kalaa_Paani , Saza_E_Kala_Pani , Manohar , Manohar , Intimacy , Khatarnak_Khel , Sati_Ansuya , Mann_Ka_Meet , Savitri , Bhagwan_Balaji , Road_to_Perdition , Akhiri_Intaqam , Narasinh_Avatar , Kamyab , Mera_Farz , Ayodhya_Ka_Raja , Jamai_Babu , En_Thangai_Kalyani , Ladki , Triya_Rajya , Ramayana , Rangeen_Duniya , Insaaf_Ki_Pukar , Maang_Bharo_Sajana , Purani_Haveli , Purana_Mandir_2 , Saamri , Veerana , Durga_Mata , Bhakti_Mahima , The_Pornographer , Husn_Ka_Ghulam , Rajrani_Mira , Zor , Catch_Me_If_You_Can , Ghar_Ki_Laxmi , Kuldipak , Misserka_Khazana , The_Girl_Next_Door , Shuk_Rambha , Barrister_Ki_Bibi , Battle_Royale , Biwi_O_Biwi , Khatarnak_Khiladi , Nimo_dhumdhana , Hollywood_Sex_Fantasy , Kill_Bill , H_S_Rawails_Mere_Mehboob , Sagai , Shagoofa , Vijaykumar , Zidd , Asra , Aatish_Feel_the_Fire , Black_Angel , Bismil_Ki_Aarzoo , Haseena_Maan_Jayegi , Hasina_Maan_Jayegi , Papi_Gudia , Jab_Jab_Pyaar_Hua , Ramayana , Ajnabee , Anand_Ashram , Lalkar , Phir_Subah_Hogi , Angaarey , A_Beautiful_Mind , Chhum_Chhama_Chhum , Jeevan_Jyoti , Raja_Ki_Ayegi_Baraat , Bewafa_Ashq , Daku_Hasina , Dr_Babasaheb_Ambedkar , Kab_Kyon_Aur_Kahan , Daagh_The_Fire , Rasila_Premi , Mujhse_Dosti_Karoge! , Do_Hazaar_Ek , Gul_Bakavali , Mehndi , Narasimham , Policewala_Gunda , tamasha , panipath , hathi_mere_sathi , ramleela , war , student_of_the_year , shadi_me_jaroor_ana , yariyaan , namaste_londan , baggi , kahani , manat , bajarangi_bhaijaan , race , kick , wanted , prem_ratan_dhan_payo , my_name_is_khan , jab_tak_hai_jaan , kedarnath , dil_bechara , chhichhore , love_aaj_kal , ajab_pem_ki_gajab_kahani , pk , dangal , secret_superstar , makkhi , suryavansham , dhishoom , muder , jism , wajah_tum_ho , rais , section_375 , pink , kill_dill , raja_babu , tanhaji , padmavat , singam , sub_mangal_savdhan , gulabo ,shoot_out_at_vadala , dhamal , golmaal , angregi_mediam , bagbaan , badsha , bang_bang , malang , kalank , gangajal , sonu_ke_titu_ki_sweety , chenai_express , raone , 3_idiots , krish , raees , om_santi_om , don , agneepath , kabir_shing , bhootnath , fanaa , bajirao_mastani , dilwale , ramaiya_vastavaiya , bolbachan , devdas , prem_leela , chak_de_india , aamdani_athani_kharcha_rupaiyaa , bahubali , takdeer , blackmail ,flying_jatt , good_news , dhadak , kal_ho_na_ho , khiladi_786 , raazi , m_s_dhoni , haider , sanju , sholay , new_york , super30 , agent_vinod , kesari , talash , tiger , tare_jamin_par , vivah , himatvala , chhelo_divash , su_thayu ,"     
        global ch
        ch="a"
        con = sql.connect('user.list')
        cur = con.cursor()
        try:
            cur.execute("""CREATE TABLE username(user text,score integer)""")
        except:
            print("table is alr ex")

        con.commit()
        con.close()
        return kv

if __name__ == "__main__":
    startgame().run()




