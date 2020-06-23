def checkSpecialKill(imgbox,imgname):
	specialHightLight=[]
	killway={
		'kill':'',
		'grenade':'',
		'smoke':'',
		'headshot':'',
		'penetration':'',
		'cardiac':'',
		'nitro':'',
		'airjab':''
	}
	for i , box in enumerate(imgbox):
		pts = np.array(box).reshape((-1,1,2))
		cv2.polylines(crop_im,[pts],True,(0,255,255),2)
		newim = affine(im,box,imfn,i,120,32)
		text = recogh_model.infer([newim])
		if text != '':
			cv2.putText(padding_image, text, (pts[1,0,0],20*(i+1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1, cv2.LINE_AA)
			res_im = np.concatenate((padding_image, crop_im), axis=0)
			cv2.imwrite("output/{}_text.png".format(imname),res_im)
			if text == 'kill':
				killway['kill']= pts
			elif text == 'smoke':
				killway['smoke'] = pts
			elif text == 'grenade':
				killway['grenade'] = pts
			elif text == 'cardiac':
				killway['cardiac'] = pts
			elif text == 'head':
				killway['headshot']=pts
			elif text == 'penetration':
				killway['penetration']=pts
			elif text == 'nitro':
				killway['nitro']=pts
			elif text == 'airjab':
				killway['airjab']=pts
			
	if  killway['kill']  is not '':
		killpointy = int(killway['kill'][0][0][1])
		if  killway['grenade'] is not '':
			if int( killway['grenade'][3][0][1])+20 > killpointy:
				specialHightLight.append('grenade')
		if  killway['smoke'] is not'':
			if int( killway['smoke'][3][0][1])+20 > killpointy:
				specialHightLight.append('smoke')
		if  killway['headshot'] is not'':
			if int( killway['headshot'][3][0][1])+20 > killpointy:
				specialHightLight.append('head')
		if  killway['penetration'] is not '':
			if int( killway['penetration'][3][0][1])+20 > killpointy:
				specialHightLight.append('penetration')
		if killway['nitro'] is not '':
			if int( killway['nitro'][3][0][1])+20 > killpointy:
				specialHightLight.append('nitro')
		if  killway['cardiac']  is not'':
			if int( killway['cardiac'][0][0][1])> killpointy:
				specialHightLight.append('cardiac')
		if  killway['airjab']  is not'':
			if int( killway['airjab'][0][0][1])> killpointy:
				specialHightLight.append('airjab')
	if len(specialHightLight) is not 0:
		print('specialHightLight   ' + imgname + ':'+str(specialHightLight))