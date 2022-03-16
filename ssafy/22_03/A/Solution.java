import java.io.*;
import java.util.StringTokenizer;

//1번
class Solution{
	//게이트 위치, 각 게이트에 대기 중인 사람 수 저장할 배열 
	static int gate[],people[];
	//낚시터 자리 수, 최소값
	static int n,answer;
	//각 게이트 방문 여부 체크 배열
	static boolean visited[];
	//dfs(깊이, 현재 이동 거리, 현재 낚시터 ->난 int로 했는데 boolean으로 하는 게 더 좋을 듯)
	static void dfs(int depth,int sum,int[]arr) {
		//가지치기 현재 이동 거리가 현재 최소값보다 크거나 같으면 더 탐색할 필요없으므로 종료
		if(sum>=answer)return;
		//모든 게이트 방문 했을 때 최소값 비교 후 갱신
		if(depth==3) {
			answer=Math.min(answer, sum);
			return;
		}
		//게이트 방문 1~3
		for(int i=1;i<=3;i++) {
			//방문 하지 않은 게이트라면 방문
			if(!visited[i]) {
				visited[i]=true;
				//현재 낚시터 배열 복사 
				int[] tempArr = copy(arr);
				//i번 게이트에 있는 사람들을 앉힘 -> 같은 거리가 두개면 오른쪽으로
				int temp = sit(i,1,tempArr);
				//다음 게이트 탐색을 위해 재귀
				dfs(depth+1,sum+temp,tempArr);				
				
				//위와 같지만 같은 거리가 두개면 왼쪽으로 
				tempArr = copy(arr);
				temp =sit(i,0,tempArr);
				dfs(depth+1,sum+temp,tempArr);				
				visited[i]=false;
			}
		}
	}
	//배열 복사 메서드
	static int[] copy(int[]target) {
		int[]result = new int[n+1];
		for(int i=1;i<=n;i++) {
			result[i]=target[i];
		}
		return result;
	}
	//사람들을 낚시터에 앉히는 메서드(현재 게이트 넘버, mode 1:오른쪽 우선, mode 0: 왼쪽 우선, arr:현재 낚시터 상태)
	static int sit(int gateNum,int mode,int[]arr) {
		//gateNum번째 게이트 사람들의 이동 거리
		int result =0;
		//gateNum번째 게이트 위치
		int pos = gate[gateNum];
		for(int i=0;i<people[gateNum];i++) {
			int dist=0;
			boolean right=false,left=false;
			//현재 위치에서 얼마나 가야 빈 자리가 있는지 확인
			while(true) {
				if(pos+dist<=n&&arr[pos+dist]==0)right=true;
				if(pos-dist>=1&&arr[pos-dist]==0)left=true;
				if(right||left)break;
				dist++;
			}
			//오른쪽과 왼쪽으로 가는 거리가 같을 떄
			if(right&&left) {
				//mode가 1이면 오른쪽
				if(mode==1) {
					arr[pos+dist]=1;
				}
				//0이면 왼쪽
				else {
					arr[pos-dist]=1;
				}
			}
			//오른쪽만 이동가능할 때
			else if(right) {
				arr[pos+dist]=1;
			}
			//왼쪽만 이동가능할 때
			else {
				arr[pos-dist]=1;
			}
			result+=dist+1;
		}
		return result;
	}

	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		//입력 부분
		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++) {
			answer=Integer.MAX_VALUE;
			n=Integer.parseInt(br.readLine());
			int[]arr=new int[n+1];
			gate = new int[4];
			people = new int[4];
			visited = new boolean[4];
			for(int i=1;i<4;i++) {
				st=new StringTokenizer(br.readLine());
				gate[i]=Integer.parseInt(st.nextToken());
				people[i]=Integer.parseInt(st.nextToken());
			}
			//dfs실행(시작 depth 0, 시작 이동 거리 0, 초기 낚시터 상태 모두 0이고 길이가 n)
			dfs(0,0,arr);
			System.out.println("#"+t+" "+answer);
		}
	}
}
