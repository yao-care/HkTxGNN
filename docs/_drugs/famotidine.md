---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 5
---

# Famotidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Famotidine：從胃酸分泌抑制到消化道潰瘍與逆流疾病

## 一句話總結

Famotidine 是一種高選擇性 H2 受體拮抗劑，透過阻斷胃壁細胞的組胺 H2 受體、抑制胃酸分泌，在全球廣泛應用於消化道酸相關疾病，但目前在香港無已登記許可證。TxGNN 模型識別出 **5 項消化道新適應症**——十二指腸胃逆流、十二指腸阻塞、消化性潰瘍、胃空腸潰瘍及消化性潰瘍穿孔，各項預測分數均達 **99.98% 以上**。其中消化性潰瘍（L1）具備多項多中心 RCT 直接支持，消化性潰瘍穿孔（L1）亦有 Phase 4 大型試驗（n=500）佐證。

---

## 快速總覽

### 藥物基本資訊

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Famotidine（DB00927） |
| 作用類別 | H2 受體拮抗劑（H2-receptor antagonist） |
| 香港上市 | ✗ 未上市（0 張許可證） |

### 五項預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|---------|
| #1 | 十二指腸胃逆流（Duodenogastric Reflux） | 99.99% | L3 | Hold |
| #2 | 十二指腸阻塞（Duodenal Obstruction） | 99.99% | L2 | Proceed with Guardrails |
| #3 | 消化性潰瘍（Active Peptic Ulcer Disease） | 99.98% | L1 | Proceed with Guardrails |
| #4 | 胃空腸潰瘍（Gastrojejunal Ulcer） | 99.98% | L2 | Proceed with Guardrails |
| #5 | 消化性潰瘍穿孔（Peptic Ulcer Perforation） | 99.98% | L1 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Famotidine 透過競爭性阻斷胃壁細胞基底外側膜上的組胺 H2 受體，抑制組胺、胃泌素及迷走神經刺激所誘發的胃酸分泌。相較於 cimetidine，效力強約 20 倍；相較於 ranitidine 強約 7.5–8 倍（PMID 2875864）。此外，famotidine 不影響肝臟細胞色素 P450 同功酶，藥物交互作用風險相對低，並具有較長的消除半衰期（口服給藥）。

所有 5 項預測適應症均屬「消化道酸相關疾病譜系」，機轉上具高度關聯性：

- **十二指腸胃逆流**：降低胃液酸度，減少反流液對胃黏膜的酸性損傷（間接保護，缺乏 RCT 支持）
- **十二指腸阻塞**：促進十二指腸潰瘍癒合，防止潰瘍慢性化所致之瘢痕性腸腔狹窄
- **消化性潰瘍**：直接針對核心病理（胃酸過多），臨床 RCT 最多，是最強證據適應症
- **胃空腸潰瘍**：胃繞道術後殘胃酸液侵蝕吻合口，降酸可保護吻合口黏膜
- **消化性潰瘍穿孔**：阻止 NSAID/阿斯匹靈使用者潰瘍深化進展至穿孔

目前 DrugBank MOA 詳細文件尚待補充，但上述抑酸機轉為醫學共識，現有文獻充分支持各項推論。

---

## 臨床試驗證據

### Rank 1：十二指腸胃逆流（L3）

目前無相關臨床試驗登記。

---

### Rank 2：十二指腸阻塞（L2）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00450216](https://clinicaltrials.gov/study/NCT00450216) | Phase 3 | 完成 | 906 | HZT-501（ibuprofen 800mg + famotidine 26.6mg 複方）預防 NSAID 使用者 GI 潰瘍，涵蓋十二指腸病變保護；廣義 GI 保護為主要終點，非十二指腸阻塞特定設計 |
| [NCT00450658](https://clinicaltrials.gov/study/NCT00450658) | Phase 3 | 完成 | 627 | 同 HZT-501 計畫第二試驗，提供互補人群驗證，設計目標相同 |

---

### Rank 3：消化性潰瘍（L1）

目前無 ClinicalTrials.gov 登記，但文獻已有多項 RCT 直接支持（見文獻證據）。

---

### Rank 4：胃空腸潰瘍（L2）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00557349](https://clinicaltrials.gov/study/NCT00557349) | Phase 4 | 完成 | 40 | 直接比較 Zegerid（Omeprazole/NaHCO₃）與 Famotidine 預防胃繞道術後吻合口潰瘍，為本適應症最直接臨床證據；樣本數偏小，統計效力有限 |

---

### Rank 5：消化性潰瘍穿孔（L1）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00683111](https://clinicaltrials.gov/study/NCT00683111) | Phase 4 | 完成 | 500 | 直接比較 Famotidine 與 Esomeprazole，預防急性冠心病患者（使用抗血小板藥）之潰瘍穿孔等嚴重 GI 併發症；規模大、設計嚴謹，為本適應症最相關試驗 |
| [NCT00450658](https://clinicaltrials.gov/study/NCT00450658) | Phase 3 | 完成 | 627 | HZT-501 廣義 NSAID-GI 保護，穿孔風險降低為次要安全終點 |

---

## 文獻證據

### Rank 1：十二指腸胃逆流

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | 前瞻性觀察（ICU） | World J Gastroenterol | 研究 famotidine 對危重症患者胃食道逆流及十二指腸胃食道逆流的影響與可能機轉，ICU 場域泛化性有限 |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | 敘述性評論 | Exp Clin Gastroenterol | Famotidine 20mg BID 於胃十二指腸逆流疾病早期（0–1 度，Savary-Miller 分級）的臨床與內視鏡療效 |

---

### Rank 2：十二指腸阻塞

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2816881](https://pubmed.ncbi.nlm.nih.gov/2816881/) | 1989 | RCT（陰性結果） | Am J Gastroenterol | H2 受體拮抗劑單次夜間給藥對十二指腸潰瘍球部狹窄患者治療失敗，提示球部狹窄療效有限，需設置療效監控 |
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | 案例報告 | Surg Endosc | 巨型邊緣潰瘍含阻塞、穿孔、瘻管等併發症，H2 拮抗劑作為輔助管理之一 |
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | 外科案例報告 | Surgery Today | 克隆氏病侵犯十二指腸致胃出口阻塞，手術為主，H2 拮抗劑為輔助療法 |

---

### Rank 3：消化性潰瘍

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2877912](https://pubmed.ncbi.nlm.nih.gov/2877912/) | 1987 | RCT（多中心雙盲安慰劑對照） | Gastroenterology | n=384，Famotidine 40mg HS / 40mg BID / 20mg BID 治療急性十二指腸潰瘍，三種劑量均優於安慰劑 |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT（頭對頭） | Clin Therapeutics | n=160，Famotidine 40mg vs Ranitidine 300mg；8 週癒合率 94% vs 80%，6 個月維持治療持效，NSAID/阿斯匹靈相關潰瘍亦分析 |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT（多中心多國） | Am J Med | n=1,031，19 國 68 研究者，Famotidine vs Ranitidine 治療活動性十二指腸潰瘍 |
| [2570005](https://pubmed.ncbi.nlm.nih.gov/2570005/) | 1989 | RCT | Digestion | n=119，Famotidine 40mg vs Cimetidine 800mg，西班牙四中心雙盲研究，基線特性無顯著差異 |
| [2670647](https://pubmed.ncbi.nlm.nih.gov/2670647/) | 1989 | RCT（多中心） | Digestion | n=143，Famotidine vs Ranitidine 單次夜間給藥，五中心短期治療十二指腸潰瘍 |
| [2092029](https://pubmed.ncbi.nlm.nih.gov/2092029/) | 1990 | RCT | J Assoc Physicians India | n=40，Famotidine 40mg vs Ranitidine 300mg 夜間單次給藥，4–8 週治療胃/十二指腸潰瘍 |
| [2889257](https://pubmed.ncbi.nlm.nih.gov/2889257/) | 1987 | 對照臨床試驗（靜脈） | Scand J Gastroenterol Suppl | 靜脈 Famotidine 治療消化性潰瘍及應力性潰瘍所致上消化道出血，探討重症場域適用性 |
| [8458053](https://pubmed.ncbi.nlm.nih.gov/8458053/) | 1993 | 臨床試驗 | Clin Therapeutics | n=71/85，Famotidine 40mg HS 單劑量治療 NSAID/阿斯匹靈相關胃潰瘍與特發性胃潰瘍，8 週癒合結果比較 |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | 回顧 | Hepato-gastroenterology | Famotidine 40mg HS 維持約 1/3 pH 讀數≥3.5、降低胃蛋白酶活性，臨床試驗癒合率文獻彙整 |
| [34798155](https://pubmed.ncbi.nlm.nih.gov/34798155/) | 2022 | 實驗（製劑研究） | Int J Pharmaceutics | Famotidine 固體自奈米乳化藥物遞送系統（SNEDDS）顯著改善消化性潰瘍療效，解決水溶性不佳問題 |

---

### Rank 4：胃空腸潰瘍

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1428035](https://pubmed.ncbi.nlm.nih.gov/1428035/) | 1992 | RCT | Indian J Gastroenterol | n=129，Omeprazole 20mg vs Famotidine 40mg；2 週癒合率 74% vs 34.3%（p<0.001），4 週 97.3% vs 75.8% |
| [8218758](https://pubmed.ncbi.nlm.nih.gov/8218758/) | 1993 | RCT | Aliment Pharmacol Ther | n=60，Omeprazole vs Famotidine；2 週癒合率 77% vs 40%，4 週 93% vs 80%；Omeprazole 更快緩解疼痛 |
| [3075106](https://pubmed.ncbi.nlm.nih.gov/3075106/) | 1988 | RCT（短/長期） | Acta Gastroenterol Latinoam | Famotidine vs Ranitidine 短期療效相當（癒合率約 83–100%）；Famotidine 20mg HS 維持 48 週復發率 38% vs 安慰劑 78% |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT（頭對頭） | Clin Therapeutics | Famotidine vs Ranitidine，十二指腸潰瘍 8 週癒合率 94% vs 80%，提供胃空腸潰瘍間接旁證 |
| [3905468](https://pubmed.ncbi.nlm.nih.gov/3905468/) | 1985 | RCT（雙盲安慰劑對照） | Digestion | 奧地利/德國多中心，n=65，Famotidine 40mg HS vs 安慰劑，良性胃潰瘍 4–8 週癒合率差異顯著 |
| [7594335](https://pubmed.ncbi.nlm.nih.gov/7594335/) | 1995 | 對照研究（EUS） | J Clin Gastroenterol | n=24，Lansoprazole vs Famotidine 胃潰瘍；EUS 評估 4 週癒合率 80% vs 67%，Lansoprazole 略優 |
| [7594320](https://pubmed.ncbi.nlm.nih.gov/7594320/) | 1995 | 轉譯/臨床 | J Clin Gastroenterol | Lansoprazole vs Famotidine 對胃潰瘍邊緣 bFGF 水平之影響，Lansoprazole 更有效上調 bFGF 促癒合 |
| [2875864](https://pubmed.ncbi.nlm.nih.gov/2875864/) | 1986 | 藥理回顧 | Drugs | Famotidine 首篇完整藥理與臨床試驗總覽，確立 20mg BID / 40mg HS 的療效基礎及安全性概況 |
| [2573505](https://pubmed.ncbi.nlm.nih.gov/2573505/) | 1989 | 回顧（更新版） | Drugs | Famotidine 1989 年更新，比 cimetidine 強 20–50 倍、比 ranitidine 強 8 倍，安慰劑對照療效確立 |
| [2883883](https://pubmed.ncbi.nlm.nih.gov/2883883/) | 1987 | 臨床研究 | Am J Gastroenterol | Famotidine 靜注不影響肝臟血流量，可安全用於慢性肝病合併消化性潰瘍患者，顯示特殊族群兼容性 |

---

### Rank 5：消化性潰瘍穿孔

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19837071](https://pubmed.ncbi.nlm.nih.gov/19837071/) | 2010 | RCT（陰性結果） | Gastroenterology | Famotidine 劣於 Pantoprazole 預防阿斯匹靈相關潰瘍復發/出血，高穿孔風險族群應優先考慮 PPI |
| [10063300](https://pubmed.ncbi.nlm.nih.gov/10063300/) | 1998 | 外科世代 | J Indian Med Assoc | 穿孔十二指腸潰瘍單純縫合閉合後的藥物療法效果評估，H2 拮抗劑為術後抑酸維持選項 |
| [19391208](https://pubmed.ncbi.nlm.nih.gov/19391208/) | 2009 | 回顧 | Khirurgiia | 出血及穿孔性胃十二指腸潰瘍的抑酸治療策略，H2RA 與 PPI 定位比較 |
| [21954519](https://pubmed.ncbi.nlm.nih.gov/21954519/) | 2011 | 回顧/指引評論 | Prescrire Int | 高風險患者 NSAID 使用應加用抗潰瘍藥以降低出血、穿孔、阻塞風險；H2RA 證據評估 |
| [21387691](https://pubmed.ncbi.nlm.nih.gov/21387691/) | 2011 | 回顧 | Nihon Rinsho | 低劑量阿斯匹靈 GI 損傷管理策略，穿孔為主要關注結果之一，H2RA 的適用族群討論 |
| [10379475](https://pubmed.ncbi.nlm.nih.gov/10379475/) | 1999 | 回顧 | Ital J Gastroenterol Hepatol | NSAID 胃病管理，無法停藥時 PPI 為首選、H2RA 為替代；停藥後任何抑酸劑均可有效癒合 |
| [12658910](https://pubmed.ncbi.nlm.nih.gov/12658910/) | 2003 | 流行病學研究 | Wien Klin Wochenschr | 奧地利 NSAID 不良反應盛行率調查，穿孔為 GI 嚴重不良事件之一，確立高風險族群 |
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | 案例報告 | Surg Endosc | 巨型邊緣潰瘍含穿孔、瘻管併發症，H2 拮抗劑在術前/術後的輔助角色 |
| [2500018](https://pubmed.ncbi.nlm.nih.gov/2500018/) | 1989 | 動物實驗 | Am J Med | 豬膽管結紮模型，Sucralfate 有效而 Famotidine 無效預防潰瘍，提示特定膽酸相關場域中抑酸機轉有限制 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

### 各適應症決策建議

| 適應症 | 決策 | 關鍵守護措施 |
|--------|------|------------|
| 十二指腸胃逆流（L3） | **Hold** | 僅有 2 篇觀察性文獻，ICU 場域泛化性有限，缺乏 RCT；需先設計可行性研究 |
| 十二指腸阻塞（L2） | **Proceed with Guardrails** | 現有試驗非主要終點；球部狹窄患者療效可能有限（PMID 2816881 陰性結果）；需療效監控守護 |
| 消化性潰瘍（L1） | **Proceed with Guardrails** | 現代指引以 PPI 為一線治療，Famotidine 定位為二線或 PPI 不耐受者替代方案；處方時需說明相對療效差距 |
| 胃空腸潰瘍（L2） | **Proceed with Guardrails** | NCT00557349 樣本數偏小（n=40）；若 PPI 優越性顯著，Famotidine 應列為 PPI 禁忌時的二線選擇 |
| 消化性潰瘍穿孔（L1） | **Proceed with Guardrails** | PMID 19837071 明確顯示 Famotidine 劣於 PPI，高穿孔風險族群（NSAID/阿斯匹靈使用者）PPI 優先；Famotidine 適用於 PPI 禁忌情境 |

**總體決策：Proceed with Guardrails（消化性潰瘍及消化性潰瘍穿孔為優先推進適應症）**

**理由：**
Famotidine 在消化性潰瘍（L1）有 ≥2 項多中心 RCT 直接支持，在消化性潰瘍穿孔（L1）有 Phase 4 大型試驗（NCT00683111，n=500）佐證，整體證據充分。然而，所有適應症均面臨 **PPI 優越性挑戰**，Famotidine 的定位應聚焦於：PPI 禁忌或不耐受患者的替代方案、低至中風險患者的短期輔助療法，以及急性場域（ICU、術後）的靜脈制酸選項。

**若要推進需要：**
- 補充 DrugBank MOA 詳細文件及藥物類別分類（API 查詢）
- 補充香港（Department of Health）仿單警語、禁忌症及 DDI 資料
- 確認香港市場實際供應狀況（未上市原因：尚未申請許可、已停產或資料缺漏）
- 針對 PPI 不耐受或禁忌亞族群設計特定臨床監控計畫
- 對十二指腸胃逆流（L3）設計可行性研究或系統性回顧，補充 RCT 層級證據後再重新評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

