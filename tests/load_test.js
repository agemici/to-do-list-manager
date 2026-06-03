import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  vus: 10, // Aynı anda 10 sanal kullanıcı
  duration: '10s', // 10 saniye boyunca istek atacak
};

export default function () {
  const res = http.get('http://host.docker.internal:8000/todos/');
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}