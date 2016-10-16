```sql
create user 'lego'@'localhost' identified by 'lego';
CREATE database lego;
grant all on lego.* to 'lego'@'localhost' identified by 'lego';
```