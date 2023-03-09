var myString: string = 'Hello world'
var num: number = 3

let strArr: string[] = ['dasasad','ass']

let asd: [string, number[], null] = ['3',[4], null];


// Functions
function getName(name1:string, name2?:string):string{
    return name1+name2
}

getName('3')

// Interfaces

interface ITodo {
    title:string,
    text:string,
    count:number
}

function showTodo(too: ITodo) : ITodo{
    return too;
}

// Class

class User {
    protected name: string
    public email:string
    private age:number
    

    constructor(name:string, email:string, age:number){
        this.name = name
        this.email = email
        this.age = age
    }

    register(){
        return this.email
    }

    getAge():number {
        return this.age
    }

    payInvoice() {
        console.log(this.age)
    }
}

class Member extends User {
    id : number

    constructor(id:number, name:string, email:string, age:number){
        super(name, email, age)
        this.id=id
    }

    payInvoice() {
        super.payInvoice()
    }
}

const user1 = new User('ricardo', 'rrojas48@itfip.edu.co', 18)

console.log(user1.getAge())


