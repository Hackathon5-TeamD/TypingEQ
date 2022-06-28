import { useState } from "react";
import axios from "axios";

// const Url = `http://localhost:3001`;
// const Url = `http://192.168.0.102:5000`;
// const Url = `http://127.0.0.1:5000`;
const Url = `http://localhost:5000`;

export const useGame = () => {
  const [jaTerm, setJaTerm] = useState("");
  const [roTerm, setRoTerm] = useState("");
  const [isAlertLoading, setAlsertLoading] = useState(false);

  const fetchGame = () => {
    setAlsertLoading(true);
    axios
      .get(`${Url}/terminologie/1`)
      .then((res) => {
        console.log(res.data);

        // サーバーから取ってきた問題をstate(配列)に入れる
        setRoTerm(res.data[0]["description_ro"]);
        setJaTerm(res.data[0]["description_ja"]);
      })
      .catch((err) => {
        console.log(err);
      })
      .finally(() => {
        setAlsertLoading(false);
      });
  };
  return { jaTerm, roTerm, fetchGame, isAlertLoading, setAlsertLoading };
};
