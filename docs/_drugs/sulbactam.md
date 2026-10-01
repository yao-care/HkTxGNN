---
layout: default
title: Sulbactam
parent: 中證據等級 (L3-L4)
nav_order: 822
evidence_level: L3
indication_count: 1
---

# Sulbactam
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Sulbactam：從 β-內醯胺酶抑制劑（抗菌複方成分）到細菌性關節炎

## 一句話總結

Sulbactam 是 β-內醯胺酶抑制劑，常與 ampicillin、cefoperazone 等抗生素組成複方，用於抗菌治療。
TxGNN 模型預測它可能對**細菌性關節炎 (Bacterial Arthritis)** 有效，但目前**沒有臨床試驗登記**，只有**20 篇檢索文獻**，其中約 10 篇與主題較相關，且多為 1980 年代的小型研究與病例報告。
原適應症資料在輸入中缺漏，因此無法確認香港核准的適應症文字。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 細菌性關節炎 (Bacterial Arthritis) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。以下說明來自一般藥理知識，並未對照輸入資料驗證。Sulbactam 是不可逆的 class A β-內醯胺酶抑制劑，也能結合 *Acinetobacter baumannii* 的 PBP，因此本身對該菌有活性。

與 ampicillin 合用時，它能恢復對產 β-內醯胺酶的金黃色葡萄球菌、腸內菌科細菌與厭氧菌的涵蓋範圍。這些正是細菌性關節炎的常見致病菌，所以在機轉上，這個預測合理。

需要留意，0.998 的高分很可能反映的是「抗菌藥物類別」的關聯，而不是新的作用機轉。這個預測比較像傳統抗感染用途的延伸，不算真正跨領域的老藥新用。

另外，文獻中的臨床資料幾乎都是 **ampicillin/sulbactam 複方**，並非 sulbactam 單獨使用，解讀時要注意這一點。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2677956](https://pubmed.ncbi.nlm.nih.gov/2677956/) | 1989 | RCT | Pediatr Infect Dis J | 以 2:1 隨機分配，比較 ampicillin/sulbactam 與 ceftriaxone 治療兒童軟組織感染（105 人）、化膿性關節炎（11 人）與骨髓炎（9 人）。摘要未完整提供療效結果 |
| [3026009](https://pubmed.ncbi.nlm.nih.gov/3026009/) | 1986 | 開放式比較試驗 | Rev Infect Dis | 比較 sulbactam/ampicillin（13 人）與 cefotaxime（9 人）作為骨、關節、軟組織感染的起始治療。前者全部病人獲得臨床治癒或改善 |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | 臨床試驗 | Rev Infect Dis | 9 名兒童骨髓炎／化膿性關節炎，先靜脈注射 sulbactam/ampicillin，再改口服 sultamicillin。已知致病菌皆敏感，且所有病人血清殺菌力價達 1:8 以上 |
| [3252119](https://pubmed.ncbi.nlm.nih.gov/3252119/) | 1988 | 臨床試驗 | Mikrobiyol Bul | 84 名各類感染病人接受 ampicillin/sulbactam，其中 5 人為化膿性關節炎與骨髓炎 |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | 比較新舊抗生素治療多重抗藥菌感染的仿單外使用與正式建議 |
| [16269877](https://pubmed.ncbi.nlm.nih.gov/16269877/) | 2005 | Review | Acta Orthop Traumatol Turc | 化膿性關節炎的診斷與起始抗生素治療方案 |
| [1745624](https://pubmed.ncbi.nlm.nih.gov/1745624/) | 1991 | 體外藥敏研究／回顧 | Pharmacotherapy | 比較 ampicillin-sulbactam 與 ticarcillin-clavulanate 的體外活性及臨床療效 |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | 回溯性世代研究 | Clin Lab | 分析 4 歲以下兒童骨關節感染的致病菌分布與抗藥性 |
| [9263167](https://pubmed.ncbi.nlm.nih.gov/9263167/) | 1997 | Case report | J Rheumatol | 貓咬傷後 *Pasteurella multocida* 感染性關節炎合併痛風，以 ampicillin/sulbactam 加關節抽吸治療後痊癒 |
| [16148860](https://pubmed.ncbi.nlm.nih.gov/16148860/) | 2005 | Case report | Pediatr Infect Dis J | 4 歲女童 *Fusobacterium necrophorum* 化膿性關節炎，ampicillin-sulbactam 治療後復發，改用 meropenem 加 clindamycin 才根除 |

## 香港上市資訊

目前共有 8 張許可證，以下列出 5 張主要許可證。輸入資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-56071 | KINTAMVY FOR INJ 1.5G | JINDUN PHARMA (H.K.) LIMITED |
| HK-68971 | XACDURO POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION | ZAI LAB (HONG KONG) LIMITED |
| HK-61003 | CEFOPERAZONE AND SULBACTAM FOR INJECTION 1G (SHENZHEN LIJIAN) | CEUTICAL TRADING COMPANY LIMITED |
| HK-56893 | NASPALUN FOR INTRAVENOUS INJ | MAIN LIFE CORP LTD |
| HK-63480 | SITANDING POWDER FOR SOLUTION FOR INJECTION 1G | JINDUN PHARMA (H.K.) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有登記的臨床試驗，文獻多為 1980 年代以 ampicillin/sulbactam 複方進行的小型研究與病例報告。
- 香港仿單的警語與禁忌症資料缺漏，屬於阻擋性缺口（Blocking），無法進入安全性篩選。
- 這個預測比較像傳統抗感染用途的延伸，系統建議等級為「研究問題（Research Question）」。

**若要推進需要：**
- 取得香港衛生署的仿單，確認警語、禁忌症與現有核准適應症。
- 補齊 DrugBank 的作用機轉與原適應症資料。
- 確認細菌性關節炎是否已被現有 ampicillin/sulbactam 的核准適應症涵蓋，避免重複評估。
- 對照現行化膿性關節炎治療指引與本地抗藥性資料，釐清 sulbactam 的實際定位。
- 查詢 ICTRP 與區域試驗註冊庫，確認是否有進行中的相關試驗。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

