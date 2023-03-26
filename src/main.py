from App import *

def main():
    handler = StandardHandler(45)
    result = handler.handleRequest(100.0)
    try:
        print(result)
    except:
        print("Result was None")
    #app = App()
    #display window 
    #app.win.mainloop()



if __name__ == "__main__":
    main()