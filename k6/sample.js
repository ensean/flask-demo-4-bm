import http from "k6/http";

export let options = {
    vus: 5,
    stages: [
        { duration: "10m", target: 50 },
    ],
    ext: {
        loadimpact: {
            projectID: xxxx,
            // Test runs with the same name groups test runs together
            name: "m5-uuid"
        }
    }
};

export default function () {
    let response = http.get("http://172.31.46.126:8000/uuid");
};