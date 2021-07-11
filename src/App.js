import React, { useEffect, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import {
  TableContainer,
  TableCell,
  Table,
  TableRow,
  TableHead,
  TableBody,
  IconButton,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
} from "@material-ui/core";
import "./App.css";

import { ArrowBack, ArrowForward } from "@material-ui/icons";

function App() {
  const [classDetails, setClassDetails] = useState([]);
  const [loading, setLoading] = useState(true);
  const [classes, setClasses] = useState([]);
  const [currentHigh, setCurrentHigh] = useState(10);
  const [currentLow, setCurrentLow] = useState(0);
  const [currentClass, setCurrentClass] = useState();

  const handleChange = (event) => {
    setCurrentClass(event.target.value);
    console.log(currentClass);
  };

  useEffect(() => {
    fetch("api/class/MWR")
      .then((response) => response.json())
      .then((data) => {
        const students = [];
        for (const key in data) {
          if (Object.hasOwnProperty.call(data, key)) {
            const student = data[key];
            students.push(student);
          }
        }
        setClassDetails(students);
      })
      .catch((err) => console.log(err))
      .finally(() => {
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    fetch("api/classes")
      .then((response) => response.json())
      .then((data) => {
        setClasses(data["classes"]);
      })
      .catch((err) => console.log(err));
  }, []);

  if (loading) {
    return <p>Data is loading...</p>;
  }
  return (
    <div className="App">
      <div className="pagination-buttons">
        <IconButton
          onClick={() => {
            if (currentLow > 0) {
              setCurrentHigh(currentHigh - 10);
              setCurrentLow(currentLow - 10);
            }
          }}
        >
          <ArrowBack fontSize="large" />
        </IconButton>
        <FormControl variant="outlined">
          <InputLabel id="demo-simple-select-outlined-label">
            Class Name
          </InputLabel>
          <Select
            defaultValue=""
            labelId="demo-simple-select-outlined-label"
            id="demo-simple-select-outlined"
            value={currentClass}
            onChange={handleChange}
            label="Class Name"
            className="className"
          >
            <MenuItem value="">
              <em>None</em>
            </MenuItem>
            {classes.map((className) => {
              return (
                <MenuItem key={className} value={className}>
                  {className}
                </MenuItem>
              );
            })}
          </Select>
        </FormControl>
        <IconButton
          onClick={() => {
            if (currentHigh < classDetails.length) {
              setCurrentHigh(currentHigh + 10);
              setCurrentLow(currentLow + 10);
            }
          }}
        >
          <ArrowForward fontSize="large" />
        </IconButton>
      </div>
      <TableContainer>
        <Table className="content-table">
          <TableHead>
            <TableRow>
              {Object.keys(classDetails[0])
                .reverse()
                .map((title) => {
                  return <TableCell key={title}>{title}</TableCell>;
                })}
            </TableRow>
          </TableHead>
          <TableBody>
            {classDetails.map((student, index) => {
              if (index >= currentLow && index <= currentHigh) {
                return (
                  <TableRow key={uuidv4()}>
                    {Object.keys(classDetails[0])
                      .reverse()
                      .map((header) => {
                        return (
                          <TableCell key={uuidv4()}>
                            {student[header]}
                          </TableCell>
                        );
                      })}
                  </TableRow>
                );
              }
              return null;
            })}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default App;
