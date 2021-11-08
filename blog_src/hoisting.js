this.num = 1;

const a = () => {
  //  this.num = 2;
  b();
};

const b = () => {
  //  this.num = 3;
  console.log(this.num);
};

a(); // 1
b(); // 1
