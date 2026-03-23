# HTML 제품 기획 보고서 출력

사용자가 "보고서를 만들어 주세요"라고 말하거나 마지막 단계 내용이 맞다고 확인할 때 트리거됩니다.

## 디자인 사양

**모던 디자인 스타일**을 사용하세요 — 단일 HTML 파일(CSS와 JS 완전 인라인), 오프라인 열람 보장.

**전체 스타일:**
- 그라데이션 배경 Hero 섹션 (모드, 독자, 날짜 라벨 포함)
- 카드 기반 레이아웃 (둥근 모서리 + 그림자), 각 섹션이 독립적 정보 카드
- 명확한 타이포그래피 계층과 편안한 가독성 간격
- 반응형 디자인, 모바일에서 부드러운 읽기

**색상 체계:**
- 주요: 딥 블루 `#1a1a2e` → `#16213e` → `#0f3460`
- 액센트: `#e94560` 또는 `#533483`
- 콘텐츠 영역 배경: `#f8f9fa`, 카드: 흰색 + `box-shadow`

**폰트:** Google Fonts CDN에서 Inter를 먼저 로드, 시스템 폰트로 폴백:
```css
/* <head>에 */
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">

/* CSS에 */
font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
```
> 이것이 유일한 허용된 외부 CDN 의존성입니다. Google Fonts를 사용할 수 없어도 페이지는 정상 렌더링됩니다.

## 페이지 구조 (완료된 단계를 기반으로 동적 렌더링)

```
┌──────────────────────────────────────────────────────────────┐
│  Hero 섹션 (제품명, 원라이너, 모드, 독자, 날짜)                    │
├──────────────────────────────────────────────────────────────┤
│  목차 네비게이션 (고정, 완료된 것만 표시)                           │
├──────────────────────────────────────────────────────────────┤
│  🧭 전략 섹션 (완료된 경우)                                      │
│     ├─ Strategy Blocks 계층 다이어그램                           │
│     ├─ Rumelt의 좋은 전략의 핵심 (진단/방침/행동)                  │
│     └─ Shreyas의 제품 업무 3단계                                │
│  ✅ 기회 점검 섹션 (완료된 경우)                                   │
│  🔍 디스커버리 섹션 (완료된 경우)                                  │
│     ├─ Persona 테이블 (카드 스타일 테이블)                        │
│     ├─ Persona 카드 (Persona당 하나)                            │
│     ├─ JTBD 분석표 (4가지 유형)                                 │
│     ├─ Opportunity Solution Tree (시각적 트리)                   │
│     └─ User Journey Map (개요 + 아코디언 상세)                   │
│  🎯 Define 섹션 (완료된 경우)                                    │
│     ├─ 페인포인트 요약 테이블                                     │
│     ├─ April Dunford 포지셔닝 프레임워크 카드                      │
│     ├─ HMW 질문 카드 (JTBD 유형 태그 포함)                       │
│     └─ 기회 평가 테이블 (기회비용 관점)                            │
│  💡 Develop 섹션 (완료된 경우)                                   │
│     ├─ PR-FAQ 카드 (보도자료 형식 시뮬레이션)                      │
│     ├─ 솔루션 아이디에이션 (3열 병렬 카드)                         │
│     ├─ Pre-mortem 리스크 테이블 (높음/중간 리스크 색상 코딩)         │
│     ├─ GEM 매트릭스 + Impact/Effort 사분면 차트                   │
│     ├─ RICE 우선순위 테이블 (완료된 경우)                          │
│     ├─ User Story 테이블 (완료된 경우)                            │
│     └─ MVP 범위 (3열 카드 + Not Doing List)                     │
│  🚀 Deliver 섹션 (완료된 경우)                                   │
│     ├─ Aha Moment 정의 카드 (눈에 띄게 표시)                      │
│     ├─ North Star Metric 카드                                   │
│     ├─ 3계층 시그널 지표 테이블                                   │
│     ├─ PMF 수준 평가 (4단계 시각화 + 현재 위치 표시)               │
│     ├─ GTM 전략 (채널 선택 + 첫 100명 사용자 계획,                │
│     │  완료된 경우)                                              │
│     ├─ 비즈니스 모델 & 프라이싱 (수익 모델 + 가격 전략,             │
│     │  완료된 경우)                                              │
│     ├─ 가설 검증 계획 테이블 (완료된 경우)                          │
│     └─ 제품 스펙 요약 (3섹션 구조:                                │
│        의사결정 요약 / 실행 경계 / 심층 참조)                       │
│  ⭐ 최적 진입점 분석 (전체 로직 체인 시각화)                         │
├──────────────────────────────────────────────────────────────┤
│  푸터: 출력 날짜 + 모드 + 프레임워크 출처                           │
└──────────────────────────────────────────────────────────────┘
```

## 섹션 디자인 세부사항

**테이블 스타일링:** 지브라 스트라이프, 어두운 헤더, 둥근 모서리, 호버 하이라이트

**Persona 카드:** Persona당 하나의 카드, 페인포인트는 빨간 왼쪽 보더, JTBD는 파란/보라 색상 블록으로 강조

**Opportunity Solution Tree:** CSS 또는 경량 SVG로 트리 구조 그리기, 목표 → 기회 → 솔루션 계층을 명확히 표시

**PMF 수준 차트:** 프로그레스 바 또는 단계 다이어그램으로 4단계 표시, 사용자의 현재 위치 마킹

**PR-FAQ 카드:** 보도자료 형식 시뮬레이션, 헤드라인, 서브타이틀, 리드 문단 — 실제 문서처럼 보이게

**Pre-mortem 리스크 테이블:** 높은 리스크 항목은 빨간 경고, 중간 리스크는 노란색

**최적 진입점 로직 체인:** 전체 추론 체인 시각화, 각 노드는 작은 카드, 화살표로 연결

## 인터랙티브 효과

- `scroll-behavior: smooth` — 목차 클릭 시 부드러운 스크롤
- Intersection Observer — 스크롤 중 현재 섹션을 목차에서 하이라이트
- 카드 호버 마이크로 리프트 (`transform: translateY(-2px)` + `transition`)
- 아코디언 확장/축소 (User Journey Map 단계, `<details>/<summary>`)
- `@media print` — 인쇄 시 인터랙티브 요소 숨기기, 테이블 잘림 방지

## 중요 참고사항

- 모든 CSS와 JS는 HTML에 인라인 — Google Fonts CDN의 Inter 외 외부 의존성 없음
- 완료되지 않은 단계는 빈 섹션으로 렌더링하지 마세요 — 그냥 건너뛰기
- Hero 섹션에 "모드"와 "독자"를 표시하여 독자가 문서의 맥락을 즉시 이해하도록
- 페이지가 매우 길 수 있음 — 목차 네비게이션이 빠른 이동에 필수

## 프레임워크 출처 및 추가 참고자료 (푸터)

| 사상가 | 핵심 기여 | 출처 |
|--------|---------|------|
| Teresa Torres | Continuous Discovery, Opportunity Solution Tree | Lenny's Podcast + *Continuous Discovery Habits* |
| Shreyas Doshi | LNO Framework, Pre-mortem, 제품 업무 3단계, 기회비용 사고 | Lenny's Podcast Ep.3 |
| Gibson Biddle | DHM Model, GEM 우선순위 | Lenny's Podcast |
| April Dunford | 포지셔닝 프레임워크 | Lenny's Podcast + *Obviously Awesome* |
| Todd Jackson | 4단계 PMF 프레임워크, Four P's | Lenny's Podcast (First Round Capital) |
| Richard Rumelt | 좋은 전략 / 나쁜 전략, 좋은 전략의 핵심 | Lenny's Podcast + *Good Strategy Bad Strategy* |
| Marty Cagan | Empowered Teams, Product Discovery | Lenny's Podcast + *Inspired*, *Empowered* |
| Chandra Janakiraman | Strategy Blocks | Lenny's Newsletter (Headspace / Meta) |
| Clayton Christensen | Jobs to Be Done | *Competing Against Luck* |
| Amazon | Working Backwards / PR-FAQ | *Working Backwards* |
| Sean Ellis | Sean Ellis Score, ICE Scoring | *Hacking Growth* |
| Lenny Rachitsky | Shape / Ship / Synchronize, North Star 사고 | Lenny's Newsletter + Podcast |
