class Woman {
  constructor(name, lastname) {
    this.name = name;
    this.lastname = lastname;
  }
}

class Pornstar extends Woman {
  constructor(name, lastname, enterprise) {
    super(name, lastname);
    this.enterprise = enterprise;
  }
}

const woman1 = new Woman("Lana", "Rhoades");
const pornstar = new Pornstar("Mia", "Khalifa", "Porn Hub");

console.log(woman1);
console.log(pornstar);
