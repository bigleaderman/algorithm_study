import java.io.*;
import java.util.StringTokenizer;

public class Solution2 {
	//맵의 변 길이, 맵에 있는 몬스터 수, 정답, 맵, 현재 위치 x,y
	static int n,total,answer,map[][],curX,curY;
	//몬스터 위치
	static int[][] monster;
	//집 위치
	static int[][] house;
	//방문한 몬스터
	static boolean[] visitedM;
	//방문한 집
	static boolean[] visitedH;
	//dfs(깊이, 현재 시간)
	static void dfs(int depth,int curT) {
		//가지치기 -> 낚시터랑 같음
		if(curT>=answer)return;
		//현재 탐색 횟수가 총 몬스터수 *2 => 총 몬스터 수+총 집 수 이면 탐색 종료
		if(depth==total*2) {
			answer=Math.min(answer, curT);
			return;
		}
		//몬스터부터 방문
		for(int i=1;i<=total;i++) {
			if(!visitedM[i]) {
				visitedM[i]=true;
				//현재 위치 값 저장 -> 되돌아 올 때 원 위치로 돌려주기 위해
				int tempX = curX;
				int tempY = curY;
				//현재 시간 + 현재 위치와 방문한 몬스터사이의 거리
				int tempA=curT+getDis(monster[i][0],monster[i][1],curX,curY);
				//현재 위치를 방문한 몬스터 위치로 갱신
				curX=monster[i][0];
				curY=monster[i][1];
				//다음 몬스터 or 집 방문을 위해 dfs
				dfs(depth+1,tempA);
				//상태 복원
				curX=tempX;
				curY=tempY;
				visitedM[i]=false;
			}
		}
		//집 방문 -> 몬스터 방문 한 거랑 같은 로직
		for(int i=1;i<=total;i++) {
			if(visitedM[i]&&!visitedH[i]){
				visitedH[i]=true;
				int tempX = curX;
				int tempY = curY;
				int tempA=curT+getDis(house[i][0],house[i][1],curX,curY);
				curX=house[i][0];
				curY=house[i][1];
				dfs(depth+1,tempA);
				curX=tempX;
				curY=tempY;
				visitedH[i]=false;
			}
		}	
	}
	//맨허튼 거리 계산 
	static int getDis(int x1,int y1, int x2, int y2) {
		return Math.abs(x1-x2)+Math.abs(y1-y2);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++){
			n=Integer.parseInt(br.readLine());
			map = new int[n][n];
			monster = new int[5][2];
			house = new int[5][2];
			visitedM = new boolean[5];
			visitedH = new boolean[5];
			total = 0;
			curX=curY=0;
			answer=Integer.MAX_VALUE;
			for(int i=0;i<n;i++){
				st=new StringTokenizer(br.readLine());
				for(int j=0;j<n;j++){
					map[i][j]=Integer.parseInt(st.nextToken());
					if(map[i][j]>0) {
						monster[map[i][j]]=new int[]{i,j};
						total = Math.max(total, map[i][j]);
					}
					if(map[i][j]<0) {
						house[-map[i][j]]=new int[]{i,j};
					}
				}
			}
			dfs(0,0);
			System.out.println("#"+t+" "+answer);
		}
	}
}