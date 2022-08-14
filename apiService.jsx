import axios from "axios";
import jwt_decode from "jwt-decode";
import dayjs from "dayjs";

const baseURL = "http://localhost:8000/api/";
let authTokens = null;

if (typeof window !== "undefined") {
  authTokens = localStorage.getItem("authTokens")
    ? JSON.parse(localStorage.getItem("authTokens"))
    : null;
}

const apiService = axios.create({
  baseURL,
  headers: {
    "Content-Type": "application/json",
    // Authorization: `Bearer ${authTokens ? authTokens.access : ""}`,
  },
});

// apiService.interceptors.request.use(async (req) => {
//   if (!authTokens) {
//     if (typeof window !== "undefined") {
//       authTokens = localStorage.getItem("authTokens")
//         ? JSON.parse(localStorage.getItem("authTokens"))
//         : null;
//     }

//     req.headers.Authorization = `Bearer ${authTokens ? authTokens.access : ""}`;
//   }

//   const user = jwt_decode(authTokens ? authTokens.access : "");
//   const isExpired = dayjs.unix(user.xxp).diff(dayjs()) < 1;
//   if (!isExpired) return req;

//   // refresh token if expired
//   const response = await axios.post(`${baseURL}auth/token/refresh/`, {
//     refresh: authTokens.refresh,
//   });

//   if (typeof window !== "undefined") {
//     localStorage.setItem("authTokens", response.data);
//   }
//   req.headers.Authorization = `Bearer ${authTokens ? authTokens.access : ""}`;

//   return req;
// });

export default apiService;
