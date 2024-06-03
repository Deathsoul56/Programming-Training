//Seleccionar la Base de Datos, si no existe mongo la crea
use school;

//Añadir un documento a la base dadatos
db.students.insertOne({name: "Bob Esponja", age: 30, gpa: 3.2})
//Añadir Varios documentos a la base de datos
db.students.insertMany([{name: "Patricio", age: 38, gpa: 1.5} ,
                        {name: "Arenita", age: 27, gpa: 4.0} ,
                        {name: "Gary", age: 18, gpa: 2.5},
                        {name: "Calamardo", age: 26, gpa: 3.1},
                        {name: "Don Cangrejo", age: 45, gpa: 1.7},
                        {name: "Perlita", age: null, gpa: 2.8}
                        ]);

//Mostrar todas las bases de datos
show dbs;

//Tipos de datos en Mongo
db.students.insertOne({name: "Larry",                             //String
                       age: 30,                                         //Int
                       gpa: 3.2,                                        //Double
                       fullTime: false,                                 //Boolean
                       registerData: new Date(),                        //Date
                       gradutionDate: null,                             //Nulo
                       couses: ["Biologia", "Quimica", "Calculo"],      //JSON
                       address: {street: "123 Fake St.",
                                 city: "Fondo de Bikini",
                                 zip: 3660000},
                       pressBanca: '55Kg',
                       fechaNacimiento: new Date("1997-03-15T18:30:56")
                       });

/**********************************************************************************************************************/
//Query para encontrar todos los documentos dentro de la base Studednts
db.students.find();

//Todos los Documentos ordenados por nombres asendente
db.students.find().sort({name:1});
//Todos los Documentos ordenados por nombres dasendente
db.students.find().sort({name:-1});

//Todos los Documentos ordenados por GPA asendente
db.students.find().sort({gpa:1});
//Todos los Documentos ordenados por nombres dasendente
db.students.find().sort({gpa:-1});

//El primer Documento de Students
db.students.find().limit(1);
//Los primeros 3 Documentos de Students
db.students.find().limit(3);

//El estudiante con mayor GPA
db.students.find().sort({gpa:-1}).limit(1);
//El estudiante con menor GPA
db.students.find().sort({gpa:1}).limit(1);

/**********************************************************************************************************************/
//.find({query}, {projection})

//Buscar Bob Esponja
db.students.find({name: "Bob Esponja"});

//Buscar el GPA de 4
db.students.find({gpa: 4});

//Buscar fullTime falso
db.students.find({fullTime: false});

//Buscar el GPA de 4 con fulltime true
db.students.find({gpa: 4, fullTime: true});

//El nombre de todos los documentos
db.students.find({}, {name: true});

//El nombre de todos los documentos sin el ID
db.students.find({}, {_id: false, name: true});

//El nombre y el gpa de todos los documentos sin el ID
db.students.find({}, {_id: false, name: true, gpa: true});

/**********************************************************************************************************************/
//.Update{{filter}, {update}}

//Agregar fullTime a Bob Esponja
db.students.updateOne({name: "Bob Esponja"},
                      {$set: {fullTime: true} })
db.students.find({name: "Bob Esponja"},
                 {_id: false});

//Modificar fullTime a Bob Esponja
db.students.updateOne({_id: ObjectId("65acbba8a1ceae396c035c4d")},
                      {$set: {fullTime: false} })
db.students.find({name: "Bob Esponja"}, {_id: false});

//Eliminar Fulltime de Bob Esponja
db.students.updateOne({_id: ObjectId("65acbba8a1ceae396c035c4d")}, {$unset: {fullTime: ""}})
db.students.find({name: "Bob Esponja"}, {_id: false});

//Agregar o modificar Fulltime false a todos los documentos
db.students.updateMany({}, {$set: {fullTime: false}})
db.students.find();

//Eliminar Fulltime de Gary y Arenita
db.students.updateMany({$or: [{name: "Gary"}, {name: "Arenita"}]},
                              {$unset: {fullTime: ""}})
db.students.find({name: {$in: ["Gary", "Arenita"]}},
                 {_id: false});

//Todos los documentos sin fulltime se les asignara True
db.students.updateMany({fullTime: {$exists: false}}, {$set: {fullTime: true}})
db.students.find({}, {_id: false});

/**********************************************************************************************************************/
//.delete({quert}, {projection})

//Eliminar a Larry
db.students.deleteOne({name: "Larry"})
db.students.find({}, {_id: false});

//Eliminar todos los que tengan fulltime false
db.students.deleteMany({fullTime: false})
db.students.find({}, {_id: false});

//Eliminar todos los documentos que no tengan registerData
db.students.deleteMany({registerData: {$exists: false}})
db.students.find({}, {_id: false});
/**********************************************************************************************************************/

//Seleccionar todos los documentos que no tengan nombre Bob Esponja
db.students.find({name: {$ne: "Bob Esponja"}}, {_id: false});

//Todos los documentos que su edad sea menor estricto que 20
db.students.find({age: {$lt: 27}}, {_id: false});

//Todos los documentos que su edad sea menor o igual que 20
db.students.find({age: {$lte: 27}}, {_id: false});

//Todos los documentos que su edad sea mayor estricto que 20
db.students.find({age: {$gt: 27}}, {_id: false});

//Todos los documentos que su edad sea mayor o igual que 20
db.students.find({age: {$gte: 27}}, {_id: false});

//Todos los estudiantes que su gpa este entre 3 y 4
db.students.find({gpa: {$gte: 3, $lte: 4}}, {_id: false});

//Los Documentos con nombre bob esponja, patricio y arenita
db.students.find({name: {$in: ["Bob Esponja", "Patricio", "Arenita"]}}, {_id: false});

//Los Documentos con nombre no sean bob esponja, patricio y arenita
db.students.find({name: {$nin: ["Bob Esponja", "Patricio", "Arenita"]}}, {_id: false});
/**********************************************************************************************************************/

//Los documentos que sean fulltime y menor o igual a 26 años
db.students.find({$and: [{fullTime: true},
                 {age: {$lte: 26}}      ]});

//Los documentos que sean fulltime o menor o igual a 26 años
db.students.find({$or: [{fullTime: true},
                 {age: {$lte: 26}}      ]});

//Los documentos que NO sean fulltime y NO sean menor o igual a 26 años
db.students.find({$nor: [{fullTime: true}, {age: {$lte: 26}}]}, {_id: false} );

//Los Documentos que no sean mayor o igual a 30 años
db.students.find({age: {$lt: 30}}, {_id: false});
//Los Documentos que no sean mayor o igual a 30 años Incluye los nulos
db.students.find({age: {$not: {$gte: 30}}}, {_id: false});
/**********************************************************************************************************************/

//Cuando se busca un valor se examina la base de datos de forma lineal, documento a documento
db.students.find({name: "Larry"}, {_id: false}).explain("executionStats")

//Crear un Indice 1:ascendente    -1: descendente
db.students.createIndex({name: 1})

//Cuando se crea un indice, se busca filtrando, en este ejemplo ahora solo se revisa 1 documento
db.students.find({name: "Larry"}, {_id: false}).explain("executionStats")

//Ver los indices
db.students.getIndexes();

//Eliminar un indice
db.students.dropIndex("name_1");
/**********************************************************************************************************************/

//Mostrar las colecciones
show collections;

//Crear una coleccion con tope, un maximo de 10MB (1024B * 1000), que no contenga mas de 100 documentos y sin auto indice por ID
db.createCollection("teachers", {capped: true, size: 1024000, max: 100}, {autoIndexId: false});

//Crear una coleccion sin paremetros adicionales
db.createCollection("courses");

//Eliminar una coleccion
db.courses.drop();

/**********************************************************************************************************************/

//Agregar cursos
db.students.updateOne({name: "Bob Esponja"}, {$set: {couses: ["Algebra", "Fisica", "Electronica"]} });
db.students.updateOne({name: "Patricio"}, {$set: {couses: ["Calculo", "Fisica", "Programacion"]} });
db.students.updateOne({name: "Arenita"}, {$set: {couses: ["Calculo", "Quimica", "Fisica", "Biologia", "Algebra"]} });
db.students.updateOne({name: "Gary"}, {$set: {couses: ["Literatura", "Algebra", "Biologia"]} });
db.students.updateOne({name: "Calamardo"}, {$set: {couses: ["Musica", "Literatura", "Historia"]} });
db.students.updateOne({name: "Don Cangrejo"}, {$set: {couses: ["Emprendimiento", "Administracion", "Algebra"]} });
db.students.updateOne({name: "Perlita"}, {$set: {couses: ["Fisica", "Calculo", "Empredimiento"]} });

//Seleccionar todos los alumnos que esten en calculo
db.students.find({couses: "Calculo"}, {_id: false});

//Seleccionar todos los alumnos que esten en algebra o literatura
db.students.find({couses: {$in: ["Algebra", "Literatura"]}}, {_id: false});

/**********************************************************************************************************************/


// DataGrip permite Traducir de SQL a MongoDB
SELECT * FROM students WHERE age >= 20;

SELECT fullTime, SUM(gpa) FROM students GROUP BY fullTime;
