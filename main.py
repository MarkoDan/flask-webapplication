from website import create_app

app = create_app()

#Only if we run this file, not if we import it
if __name__ == '__main__':
    app.run(debug=True)
    
    

