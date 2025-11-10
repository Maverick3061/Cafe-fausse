const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000';

export async function fetchMenu(){
  const r = await fetch(`${API_BASE}/api/menu`);
  if(!r.ok) throw new Error('Failed to load menu');
  return r.json();
}

export async function signupNewsletter(payload){
  const r = await fetch(`${API_BASE}/api/newsletter`, {
    method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)
  });
  return r.json();
}

export async function createReservation(payload){
  const r = await fetch(`${API_BASE}/api/reservations`, {
    method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)
  });
  if(!r.ok){
    const err = await r.json().catch(()=>({error:'request failed'}));
    throw err;
  }
  return r.json();
}
