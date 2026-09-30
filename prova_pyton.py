meme_dict = {
            "cringe": "Qualcosa di eccezionalmente strano o imbarazzante",
            "lol": "Una risposta comune a qualcosa di divertente",
             # --- PAROLE DI USO COMUNE ---
            "casa": "Edificio a uso abitativo, luogo in cui una persona vive.",
            "libro": "Insieme di fogli stampati o manoscritti, rilegati insieme.",
            "tempo": "La dimensione nella quale si misura il trascorrere degli eventi.",
            "lavoro": "Attività produttiva che richiede uno sforzo fisico o mentale.",
            "amico": "Persona legata a un'altra da un sentimento di affetto e stima.",
            "viaggio": "Lo spostamento da un luogo a un altro, generalmente lontano.",
            
            # --- TECNOLOGIA E INFORMATICA ---
            "computer": "Macchina elettronica programmabile per il trattamento dei dati.",
            "internet": "Rete globale di computer collegati tra loro.",
            "codice": "Insieme di istruzioni scritte per un computer.",
            "algoritmo": "Sequenza logica di passi per risolvere un problema.",
            "software": "Insieme dei programmi che fanno funzionare un computer.",
            "database": "Archivio digitale organizzato per consultare dati rapidamente.",
            
            # --- NATURA E SCIENZA ---
            "albero": "Pianta legnosa perenne con un tronco e dei rami.",
            "stella": "Corpo celeste che brilla di luce propria nel cielo notturno.",
            "acqua": "Composto chimico liquido, trasparente e vitale per gli organismi.",
            "energia": "Capacità di un sistema di compiere un lavoro.",
            "pianeta": "Corpo celeste che orbita attorno a una stella.",
            "evoluzione": "Processo di trasformazione graduale degli organismi viventi.",
            
            # --- PAROLE PARTICOLARI E RICERCATE ---
            "serendipità": "La fortuna di fare scoperte felici per puro caso.",
            "resilienza": "Capacità di resistere e superare un periodo difficile.",
            "crepuscolo": "La luce diffusa che precede il sorgere o segue il tramonto del sole.",
            "effimero": "Qualcosa che dura solo per un brevissimo periodo di tempo.",
            "soliloquio": "Discorso che una persona fa tra sé e sé.",
            "adamantino": "Puro, limpido e resistente come il diamante."
    
        }
while True:
    
    parola = input("Scrivi una parola che non capisci (usa solo lettere minuscole!): ")
    
    if parola in meme_dict.keys():
       # Cosa fare se la parola è stata trovata?
        print(meme_dict[parola])
    else:
    # Cosa fare se la parola non è stata trovata?
        print("Non conosco questa parola...", parola)
        print("Sei sicuro/a che la parola sia corretta e in minuscolo?")
        while True:
            e_corretta = input ("1 = è tutto corretto 2 = cè un errore")
            if e_corretta == "1":
                descrizione_nuova_parola = input("Quale è il significato della parola ", parola, "?")
                meme_dict[parola] = descrizione_nuova_parola
                break
            else:
                
                print("ok")
                break
