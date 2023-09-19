# Database design

### User

|   Column name    | Data type | Note        |
|:----------------:|:---------:|-------------|
|        Id        |  String   | PRIMARY KEY |
|     Username     |  String   |             |
|      Email       |  String   |             |
|     Password     |  String   |             |
| Is_administrator |  boolean  |             |  
|     Is_block     |  boolean  |             |

### Link

|  Column name  | Data type | Note        |
|:-------------:|:---------:|-------------|
|      Id       |  String   | PRIMARY KEY |
|     Slug      |  String   |             |
|   Long_URL    |  String   |             |
| Link_password |  String   |             |
|  Click_times  |    int    |             |
|  Is_phishing  |  boolean  |             |  
|    UserId     |  String   | FOREIGN KEY |
