


<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Machine Readable Zone generator and checker</title>
  </head>
  <body>
    

    <div class="container-fluid my-2" style="width: 100%">

	<div class="row justify-content-center" style="display: none;"><div class="col-md-6">
        <h5 class="text-center">Machine Readable Zone generator and checker</h5>
	</div></div>

	<div class="row justify-content-center"><div class="col-md-6">
        <h5 class="font-weight-bold">Passports</h5>
		
		<div class="card">
		
			%if 'error' in stat:
			<div class="card-body" style="background: pink; padding: 0.5rem;">
			%else:
			<div class="card-body" style="background: aliceblue; padding: 0.5rem;">
			%end

			%if 'error' in stat:
            <div class="align-self-center">
                <div style="margin: 0;">{{stat['error']}}</div>
            </div>
            %end

			%if 'result' in stat:
            <div class="align-self-center text-center">
                <pre style="margin: 0;">{{stat['result']}}</pre>
            </div>
			%else:
				<div style="margin: 0; color: gray;">result</div>
            %end
			
			%if 'error' in stat:
			</div>
			%else:
			</div>
			%end	
		</div>

		<div class="my-2">
		</div>

        <form method="post"> 

            <div class="form-group">
                <label for="document_type">Normally 'P' for passport</label>
                %if 'document_type' in stat:
                <input type="text" class="form-control form-control-sm" id="document_type" name="document_type" value="{{stat['document_type']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="document_type" name="document_type" value="P">
                %end
            </div>

            <div class="form-group">
                <label for="country_code">3 letters code (ISO 3166-1) or country name (in English)</label>
                %if 'country_code' in stat:
                <input type="text" class="form-control form-control-sm" id="country_code" name="country_code" value="{{stat['country_code']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="country_code" name="country_code" placeholder="">
                %end
            </div>

            <div class="form-group">
                <label for="surname">Surname(s). Special characters will be transliterated</label>
                %if 'surname' in stat:
                <input type="text" class="form-control form-control-sm" id="surname" name="surname" value="{{stat['surname']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="surname" name="surname" placeholder="">
                %end
            </div>

            <div class="form-group">
                <label for="given_names">Given name(s). Special characters will be transliterated</label>
                %if 'given_names' in stat:
                <input type="text" class="form-control form-control-sm" id="given_names" name="given_names" value="{{stat['given_names']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="given_names" name="given_names" placeholder="">
                %end
            </div>

            <div class="form-group">
                <label for="document_number">Document number</label>
                %if 'document_number' in stat:
                <input type="text" class="form-control form-control-sm" id="document_number" name="document_number" value="{{stat['document_number']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="document_number" name="document_number" placeholder="">
                %end
            </div>

            <div class="form-group">
                <label for="nationality">Nationality. 3 letter code or country name</label>
                %if 'nationality' in stat:
                <input type="text" class="form-control form-control-sm" id="nationality" name="nationality" value="{{stat['nationality']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="nationality" name="nationality" placeholder="">
                %end
            </div>

            <div class="form-group">
                <label for="birth_date">Birth date YYMMDD</label>
                %if 'birth_date' in stat:
                <input type="text" class="form-control form-control-sm" id="birth_date" name="birth_date" value="{{stat['birth_date']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="birth_date" name="birth_date" placeholder="710307">
                %end
            </div>

            <div class="form-group">
                <label for="sex">Genre. Male: 'M', Female: 'F' or Undefined 'X'</label>
                %if 'sex' in stat:
                <input type="text" class="form-control form-control-sm" id="sex" name="sex" value="{{stat['sex']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="sex" name="sex" value="M" placeholder="M">
                %end
            </div>

            <div class="form-group">
                <label for="expiry_date">Expiry date YYMMDD</label>
                %if 'expiry_date' in stat:
                <input type="text" class="form-control form-control-sm" id="expiry_date" name="expiry_date" value="{{stat['expiry_date']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="expiry_date" name="expiry_date" placeholder="110725">
                %end
            </div>

            <div class="form-group">
                <label for="optional_data1">Id number. Non-mandatory field in some countries</label>
                %if 'optional_data1' in stat:
                <input type="text" class="form-control form-control-sm" id="optional_data1" name="optional_data1" value="{{stat['optional_data1']}}">
                %else:
                <input type="text" class="form-control form-control-sm" id="optional_data1" name="optional_data1" placeholder="">
                %end
            </div>

             <div class="form-group align-self-center">
                <button type="submit" class="btn btn-primary">Start</button>
            </div>
        </form>




        <form method="post"> 
                <input type="hidden" class="form-control" id="document_type" name="document_type" value="P">
                <input type="hidden" class="form-control" id="country_code" name="country_code" value="QATAR">
                <input type="hidden" class="form-control" id="surname" name="surname" value="AL-KAABI">
                <input type="hidden" class="form-control" id="given_names" name="given_names" value="ALI HAMAD ABDULLAH">
                <input type="hidden" class="form-control" id="document_number" name="document_number" value="00000000">
                <input type="hidden" class="form-control" id="nationality" name="nationality" value="QAT">
                <input type="hidden" class="form-control" id="birth_date" name="birth_date" value="710307">
                <input type="hidden" class="form-control" id="sex" name="sex" value="M">
                <input type="hidden" class="form-control" id="expiry_date" name="expiry_date" value="110725">
                <input type="hidden" class="form-control" id="optional_data1" name="optional_data1" value="12345458902">
             <div class="form-group align-self-center">
                <button type="submit" class="btn btn-warning btn-sm">Test Qatar</button>
            </div>
        </form>

        <form method="post"> 
                <input type="hidden" class="form-control" id="document_type" name="document_type" value="P">
                <input type="hidden" class="form-control" id="country_code" name="country_code" value="JPN">
                <input type="hidden" class="form-control" id="surname" name="surname" value="GAIMU">
                <input type="hidden" class="form-control" id="given_names" name="given_names" value="SAKURA">
                <input type="hidden" class="form-control" id="document_number" name="document_number" value="XS1234567">
                <input type="hidden" class="form-control" id="nationality" name="nationality" value="Japan">
                <input type="hidden" class="form-control" id="birth_date" name="birth_date" value="790220">
                <input type="hidden" class="form-control" id="sex" name="sex" value="F">
                <input type="hidden" class="form-control" id="expiry_date" name="expiry_date" value="160320">
             <div class="form-group align-self-center">
                <button type="submit" class="btn btn-success btn-sm">Test Japan</button>
            </div>
        </form>



	</div></div>




    </div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>

