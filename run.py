from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Enhanced Didactic Story Generator is running!")
    print("Open your web browser and visit: http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=True) 