<!doctype html>
<html lang="en">

<head>
	<!-- Required meta tags -->
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
		integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

	<!-- Datepicker -->
	<link rel="stylesheet" href="dist/jquery-ui/jquery-ui.css">
	<link rel="stylesheet" href="dist/jquery-ui/jquery-ui-timepicker-addon.css">

	<!-- User defined -->
	<link rel="stylesheet" href="dist/page.css">

	<title>Результаты поединков</title>
    <script crossorigin src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
    
    <!-- Don't use this in production: 
	<script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
    -->
</head>

<body>

	<div class="container-fluid my-2" style="width: 80%">

		<h3>Результаты поединков</h3>

		<form class="" method="post">
			<div class="row">

				<div class="form-group col-sm-2 align-self-end">
					<label for="datepicker1">Дата от:</label>
					%if 'datestart' in stat:
					<input type="text" class="form-control datepicker" id="datepicker1" name="datestart" value="{{stat['datestart']}}">
					%else:
					<input type="text" class="form-control datepicker" id="datepicker1" name="datestart" placeholder="Дата от">
					%end
				</div>

				<div class="form-group col-sm-2 align-self-end">
					<label for="datepicker2">Дата до:</label>
					%if 'dateend' in stat:
					<input type="text" class="form-control datepicker" id="datepicker2" name="dateend" value="{{stat['dateend']}}">
					%else:
					<input type="text" class="form-control datepicker" id="datepicker2" name="dateend" placeholder="Дата до">
					%end
				</div>

				<div class="form-group col-sm-6" style="display: none;">
					<label for="opp">Оппонент:</label>
					<select class="custom-select" id="opp" name="oppname">
						%if name == "":
							<option value="" selected disabled>please select</option>
						%end

						%for row in rows:
							%if bytes(name, 'utf-8') == row[0]: # or name == row[0].decode('utf8')
								<option value="{{str(row[1])}}" selected>{{row[0]}}</option>
							%else:
								<option value="{{str(row[1])}}">{{row[0].decode('utf8')}}</option>
							%end
						%end
					</select>
				</div>

				<div class="form-group col-sm align-self-end">
						<label for="r_from">Раунд начала:</label>
						%if 'r_from' in stat:
						<input type="text" class="form-control" id="r_from" name="r_from" value="{{stat['r_from']}}">
						%else:
						<input type="text" class="form-control" id="r_from" name="r_from">
						%end
				</div>

				<div class="form-group col-sm">
						<label for="r_num">Число строк по горизонтали:</label>
						%if 'r_num' in stat:
						<input type="text" class="form-control" id="r_num" name="r_num" value="{{stat['r_num']}}">
						%else:
						<input type="text" class="form-control" id="r_num" name="r_num" placeholder="">
						%end
				</div>
				
				<div class="form-group col-sm align-self-end" style="display: none;">
						<label for="r_f">Количество фаталити:</label>
						%if 'r_f' in stat:
						<input type="text" class="form-control" id="r_f" name="r_f" value="{{stat['r_f']}}">
						%else:
						<input type="text" class="form-control" id="r_f" name="r_f" placeholder="">
						%end
				</div>

				<div class="form-group col-sm align-self-end">
						<label for="min_sfr">Минимальный коэффициент:</label>
						%if 'min_sfr' in stat:
						<input type="text" class="form-control" id="min_sfr" name="min_sfr" value="{{stat['min_sfr']}}">
						%else:
						<input type="text" class="form-control" id="min_sfr" name="min_sfr" placeholder="">
						%end
				</div>
				
				<div class="form-group col-sm align-self-end">
				</div>
				
			</div>


			<div class="row">

				<div class="form-group col-sm-1 align-self-end">
				</div>

				<div class="form-group col-sm-3 align-self-center">
						<label for="p_col" style="margin-bottom: 0;" title="строго больше">Побед % по счету:</label>
				</div>

				<div class="form-group col-sm align-self-center">
						%if 'p_col' in stat:
						<input type="text" class="form-control" id="p_col" name="p_col" value="{{stat['p_col']}}">
						%else:
						<input type="text" class="form-control" id="p_col" name="p_col" placeholder="">
						%end
				</div>

				<div class="form-group col-sm align-self-center">
						<label for="p_grid" style="margin-bottom: 0;" title="не менее">Побед % по сетке:</label>
				</div>
				
				<div class="form-group col-sm align-self-center">

						%if 'p_grid' in stat:
						<input type="text" class="form-control" id="p_grid" name="p_grid" value="{{stat['p_grid']}}">
						%else:
						<input type="text" class="form-control" id="p_grid" name="p_grid" placeholder="">
						%end
				</div>

				<div class="form-group col-sm align-self-center">
				</div>
				
			</div>



			<div class="row">

				<div class="form-group col-sm-1 align-self-end">
				</div>

				<div class="form-group col-sm-3 align-self-center">
						<label for="v_num" style="margin-bottom: 0;">Число строк по вертикали:</label>
				</div>

				<div class="form-group col-sm align-self-center">
						%if 'v_num' in stat:
						<input type="text" class="form-control" id="v_num" name="v_num" value="{{stat['v_num']}}">
						%else:
						<input type="text" class="form-control" id="v_num" name="v_num" placeholder="">
						%end
				</div>

				<div class="form-group col-sm align-self-center">
						<label for="r_limit" style="margin-bottom: 0;">Кол. результатов:</label>
				</div>
				
				<div class="form-group col-sm align-self-center">

						%if 'r_limit' in stat:
						<input type="text" class="form-control" id="r_limit" name="r_limit" value="{{stat['r_limit']}}">
						%else:
						<input type="text" class="form-control" id="r_limit" name="r_limit" placeholder="">
						%end
				</div>
				
				<div class="form-group col-sm align-self-center">
						<button type="submit" class="btn btn-primary">Старт</button>
				</div>
				
			</div>

		
		</form>


		%if stat != {}:

		<div class="row">
			
			<div class="col-md-4">
				<div class="card">
					<div class="card-body">
						<div class="row justify-content-start">
							<div class="col-sm">Найдено игр:</div>
							<div class="col-sm">{{stat["total"]}}</div>
						</div>
						<div class="row justify-content-start" style="display: none;">
							<div class="col-sm">Успешно:</div>
							<div class="col-sm" id="label_win1">{{stat["win"]}}</div>
						</div>
						<div class="row justify-content-start" style="display: none;">
							<div class="col-sm">Проигрыш:</div>
							<div class="col-sm" id="label_lose1">{{stat["total"] - stat["win"]}}</div>
						</div>
						<hr style="display: none;" />
						<div class="row justify-content-start">
							<div class="col-sm">Успешно:</div>
							<div class="col-sm" id="label_win">{{stat["win_pcol"]}}</div>
						</div>
						<div class="row justify-content-start">
							<div class="col-sm">Проигрыш:</div>
							<div class="col-sm" id="label_lose">{{stat["total"] - stat["win_pcol"]}}</div>
						</div>
						<div class="row justify-content-start">
							<div class="col-sm">Средний % побед по счету:</div>
							<div class="col-sm align-self-center" id="label_pcol">{{stat["avg_pcol"]}}</div>
						</div>
						<div class="row justify-content-start">
							<div class="col-sm">Средний % побед по сетке:</div>
							<div class="col-sm align-self-center" id="label_pgrid">{{stat["avg_pgrid"]}}</div>
						</div>
						<div class="row justify-content-start">
							<div class="col-sm">Средний коэффициент:</div>
							<div class="col-sm align-self-center" id="label_sfr">{{stat["avg_sfr"]}}</div>
						</div>
			
					</div>
				</div>
				<div class="my-3"></div>
			</div>
			<div class="col-md">
				<div class="row">
					<div class="col-lg-6" id="calc"></div>
				</div>
			</div>
		</div>	


		

		%else:

		<div class="my-2"></div>
		<table class="table table-borderless tb-spravka" style="margin-bottom: 0em;">
			<tr>
				<td scope="col"><a href="#help" class="help" data-toggle="collapse">
				<div class="">Справка</div>
				</a></td>
			</tr>
		</table>
		<div id="help" class="collapse">
		<table class="table table-borderless tb-spravka">
			<tbody>
			<tr>
				<td>Дата от:</td>				
				<td>дата первого боя, включая этот день. Пустое поле - от самого первого боя</td>
			</tr>
			<tr>
				<td>Дата до:</td>
				<td>дата последнего боя, исключительно до этого дня. Пустое поле - до завтра</td>
			</tr>
			<tr>
				<td>Раунд начала:</td>
				<td>первый раунд подсчета Числа F, включая этот раунд. Пустое поле - с первого раунда</td>
			</tr>
			<tr>
				<td>Число строк по горизонтали:</td>
				<td>число боев (строк) в отфильтрованной таблице для подсчета Числа F. Пустое - все строки</td>
			</tr>
			<tr>
				<td>Число строк по вертикали:</td>
				<td>число раундов от Раунда начала. Пустое поле - все оставшиеся раунды в бою</td>
			</tr>
			<tr style="display: none;">
				<td>Количество фаталити:</td>
				<td>минимальное число F для попадания в таблицу результатов. Не может быть пустым</td>
			</tr>
			<tr>
				<td>Побед % по счету:</td>
				<td>Минимальный (больше) процент побед по столбцу финального результата, счета. Пустое - 50</td>
			</tr>
			<tr>
				<td>Побед % по сетке:</td>
				<td>Минимальный (не менее) процент побед в сетке в отфильтрованной таблице. Пустое - любой процент</td>
			</tr>
			<tr style="display: none;">
				<td>Минимальный коэффициент:</td>
				<td>в таблицу результатов попадут бои с коэффициентом не ниже минимального. Пустое - с любым коэффициентом</td>
			</tr>
			<tr>
				<td>Минимальный коэффициент:</td>
				<td>в таблицу результатов попадут бои с коэффициентом соперника, процент побед по столбцу финального результата которого не ниже минимального. Пустое - с любым коэффициентом</td>
			</tr>
			<tr>
				<td>Количество результатов:</td>
				<td>максимальное число строк в таблице результатов. Пустое поле - не ограничено</td>
			</tr>
			</tbody>
		</table>
		</div>
		%end


		<div class="my-3"></div>

		%if table != []:
		<table class="table table-striped table-bordered">
			<tr>
				<th scope="col">#</th>
				<th scope="col">Время</th>
				<th scope="col">Игроки</th>
				<th scope="col" style="display: none;">Результат по F</th>
				<th scope="col">Результат</th>
				<th scope="col" style="display: none;">Число F</th>
				<th scope="col">Побед % по счету</th>
				<th scope="col">Побед % по сетке</th>
                <th scope="col" style="display: none;">Коэффициент</th>
				<th scope="col">Коэффициент</th>
				<th scope="col" style="display: none;">Раунд прошла</th>
				<th scope="col">Раунд прошла</th>
			</tr>

			%for idx, row in enumerate(table):

			<tr>
				
				<!--
				<th scope="row"><a href=
									{   delete spaces   {('\info?id={}&t1={}&opp1={}&opp2={}&r_from={}&r_num={}&r_f={}').format(row['id'], row['time1'], row['opp1'], row['opp2'], stat['r_from'], stat['r_num'], stat['r_f'])}}
								>{{idx+1}}</a>
				</th>
				-->

				<td scope="row">
					<form action="/info" class="" method="post" id="myForm{{idx+1}}">
						<input type="hidden" name="id" value="{{row['id']}}">
						<input type="hidden" name="time1" value="{{row['time1']}}">
						<input type="hidden" name="time2" value="{{stat['time2']}}">
						<input type="hidden" name="opp1" value="{{row['opp1']}}">
						<input type="hidden" name="opp2" value="{{row['opp2']}}">
						<input type="hidden" name="r_from" value="{{stat['r_from']}}">
						<input type="hidden" name="r_num" value="{{stat['r_num']}}">
						<input type="hidden" name="r_f" value="{{stat['r_f']}}">
						<input type="hidden" name="fi" value="">
						<a href="javascript:{}" onclick="document.getElementById('myForm{{idx+1}}').submit();"></a>{{idx+1}}
					</form>
				</td>

				<!--https://bkstat.vip/mk/stat?clid_opp1=377353&clid_opp2=377363-->
				<td>{{row["time"][2:]}}</td>
				<td><a href="https://bkstat.vip/mk/stat?clid_opp1={{row['opp1']}}&clid_opp2={{row['opp2']}}">{{row["name"]}}</a></td>
				<td style="display: none;">{{row["rname"]}}</td>
				<td>{{row["rname_pcol"]}}</td>
				<td style="display: none;">{{row["sumF"]}}</td>
				<td>{{round(float(row["percentcol"]), 2)}}</td>
				<td>{{round(float(row["percentgrid"]), 2)}}</td>
				<td style="display: none;">{{row["sfr"]}}</td>
                <td>{{row["percentcol_sfr"]}}</td>
				<td style="display: none;">{{row["renter"]}}</td>
				<td>{{row["renter_pcol"]}}</td>
			</tr>
			%end

		</table>
		%end

		<div style="display: none;">
			<div class="my-3">debug:</div>
			%for row in debug:
			<div>{{row}}</div>
			%end
	    </div>

	</div>

	<!-- Optional JavaScript -->
	<!-- jQuery first, then Popper.js, then Bootstrap JS -->
	<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
		integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
		crossorigin="anonymous"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
		integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
		crossorigin="anonymous"></script>


	<!-- Not working with jquery slim -->
	<script type="text/javascript" src="dist/page-simple.js"></script>
	<script type="text/javascript" src="dist/jquery-ui/jquery-ui.js"></script>
	<script type="text/javascript" src="dist/jquery-ui/jquery-ui-timepicker-addon.js"></script>

	<script>

		$(function () {
			$(".datepicker").datepicker({
				dateFormat: 'yy-mm-dd',
				firstDay: 1,
				timeFormat: 'HH:mm'
			});

		});

	</script>

    <!--
	<script type="text/babel" src="dist/calc_babel.js"></script>
    -->
    <script src="dist/calc.js"></script>

</body>

</html>