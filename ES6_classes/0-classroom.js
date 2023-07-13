let ClassRoom = class {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }
}


const room = new ClassRoom(10);
console.log(room._maxStudentsSize)
