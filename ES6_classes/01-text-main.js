import ClassRoom from "./0-classroom";

test("Initialize an instance of ClassRoom set to 100", () => {
  const room = new ClassRoom(100);
  expect(room._maxStudentsSize).toBe(100);
});
