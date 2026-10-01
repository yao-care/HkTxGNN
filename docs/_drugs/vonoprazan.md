---
layout: default
title: Vonoprazan
parent: 僅模型預測 (L5)
nav_order: 926
evidence_level: L5
indication_count: 5
---

# Vonoprazan
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

# Vonoprazan：從胃酸相關疾病到活動性消化性潰瘍

## 一句話總結

Vonoprazan 是鉀離子競爭性酸阻斷劑（P-CAB），用於抑制胃酸分泌。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
目前有 **2 個臨床試驗**和 **17 篇文獻**支持這個方向。
不過文獻顯示潰瘍治療已是 vonoprazan 在多國的既有適應症，這比較像是對既有用途的確認，而非全新的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.97%（模型排名 933） |
| 證據等級 | L1（依證據包評級；登記試驗僅有上市後監測，支持力來自已發表的 RCT 與統合分析） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

香港許可證上的原適應症欄位為空白，因此本表不列原適應症。

## 為什麼這個預測合理？

Vonoprazan 是 P-CAB，作用在胃壁細胞的 H⁺/K⁺-ATPase（質子泵）。它以競爭鉀離子的方式抑制酸分泌，效果強且持久，不像質子泵抑制劑（PPI）需要酸活化。胃酸是潰瘍形成與延遲癒合的關鍵因素，所以強效抑酸在機轉上能支持潰瘍癒合。

DrugBank 的 MOA 欄位目前缺漏，但上述機轉在文獻中有清楚描述。文獻也顯示，vonoprazan 在日本已核准用於胃潰瘍與十二指腸潰瘍，並用於預防低劑量阿斯匹靈或 NSAID 引起的潰瘍復發。因此這個預測與實際用途吻合，主要價值在於確認。

另外，本次輸入資料中的原適應症為空白，香港許可證也沒有登載適應症文字。在把它當作「再利用候選」之前，應先核對藥品標示資料，確認香港核准的適應症是否已涵蓋潰瘍。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03214952](https://clinicaltrials.gov/study/NCT03214952) | 無分期（上市後監測） | 完成 | 3183 | Takecab（vonoprazan）用於胃潰瘍、十二指腸潰瘍與逆流性食道炎的真實世界安全性與有效性監測，不能證明因果療效 |
| [NCT03116841](https://clinicaltrials.gov/study/NCT03116841) | Phase 4 | 完成 | 3 | 探索 vonoprazan 20 mg 對逆流性食道炎患者睡眠障礙的影響，僅 3 人，與潰瘍關聯低 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28988197](https://pubmed.ncbi.nlm.nih.gov/28988197/) | 2018 | RCT | Gut | 與 lansoprazole 比較，評估 vonoprazan 預防長期 NSAID 治療中潰瘍復發的非劣性，並延伸評估長期安全性 |
| [28267236](https://pubmed.ncbi.nlm.nih.gov/28267236/) | 2017 | RCT | Digestive Endoscopy | 前瞻性隨機試驗，評估 vonoprazan 對內視鏡黏膜下剝離術（ESD）後人工胃潰瘍的癒合效果 |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 系統性回顧／網絡統合分析 | Am J Gastroenterol | 比較 P-CAB 與 PPI 治療 LA 分級 C/D 重度食道炎的療效與安全性（焦點為食道炎，非潰瘍） |
| [39156336](https://pubmed.ncbi.nlm.nih.gov/39156336/) | 2024 | Review | Cureus | 綜述 vonoprazan 在 GERD、消化性潰瘍與幽門桿菌感染等胃酸相關疾病的療效與安全性 |
| [26369775](https://pubmed.ncbi.nlm.nih.gov/26369775/) | 2016 | Pharmacology Review | Clin Pharmacokinet | 說明 vonoprazan 的藥動／藥效學，並提到日本核准用於胃十二指腸潰瘍及預防 NSAID／阿斯匹靈相關潰瘍 |
| [37066678](https://pubmed.ncbi.nlm.nih.gov/37066678/) | 2023 | 轉譯 PK/PD 研究 | Aliment Pharmacol Ther | 以 PK/PD 方法支持 vonoprazan 在糜爛性食道炎與幽門桿菌感染的最適劑量 |
| [32998241](https://pubmed.ncbi.nlm.nih.gov/32998241/) | 2020 | Review | Pharmaceuticals | 討論 vonoprazan 作為幽門桿菌治療成分的潛在優勢，根除可降低潰瘍復發 |
| [22512618](https://pubmed.ncbi.nlm.nih.gov/22512618/) | 2012 | 藥物探索（前臨床） | J Med Chem | 發現 TAK-438（vonoprazan），抑酸效力強於 PPI 且作用時間更長 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-68731 | VOCINTI TABLETS 10MG | TAKEDA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-68732 | VOCINTI TABLETS 20MG | TAKEDA PHARMACEUTICALS (HONG KONG) LIMITED |

兩張許可證的劑型與核准適應症文字在資料中皆為空白。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
TxGNN 分數極高，且有 RCT、統合分析與日本指引層級的文獻支持 vonoprazan 用於潰瘍。但登記試驗僅有上市後監測，香港許可證的適應症與安全性資料也缺漏，因此需有條件推進。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認核准適應症是否已涵蓋潰瘍，並補齊警語與禁忌症（目前為阻擋項目）。
- 核對藥品標示資料，確認這是既有適應症的確認，還是需要申請的新增適應症。
- 補充 DrugBank 的作用機轉資料。
- 查詢藥物交互作用（本次查詢無結果）。

另外，同一模型對 vonoprazan 的其他預測中，「無胃酸症 (achlorhydria)」在機轉上與抑酸作用相衝突，應視為偽陽性。「食道裂孔疝」則屬解剖異常，抑酸藥無法矯正，建議暫緩（Hold）。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

