// eslint-disable-next-line import/no-unresolved
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  return (Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)]).then(
    (values) => console.log(`${values[0].body} ${values[1].body}`),
  ).catch(() => console.log('Signup system offline')));
}

console.log(handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg'));
