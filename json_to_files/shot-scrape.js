({
  "appg_donations.json": JSON.stringify(window.template.data.appg_donations, null, 2),
  "appgs.json": JSON.stringify(window.template.data.appgs, null, 2),
  "member_appgs.json": JSON.stringify(window.template.data.member_appgs, null, 2),
  "parties.json": JSON.stringify(window.template.data.parties, null, 2),
  "party_donations.json": JSON.stringify(window.template.data.party_donations, null, 2),
  "payments.json": JSON.stringify(window.template.data.payments, null, 2),
  "members.json": JSON.stringify(
    window.template.data.members.map(
      ({ id, name, gender, constituency, party_id, short_name, status }) => ({
        id,
        name,
        gender,
        constituency,
        party_id,
        short_name,
        status,
      })
    ), null, 2
  )
})