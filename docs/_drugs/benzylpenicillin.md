---
layout: default
title: Benzylpenicillin
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 7
---

# Benzylpenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Benzylpenicillin：從細菌感染到冠周炎 (Pericoronitis)

## 一句話總結

Benzylpenicillin（青黴素 G）是經典的青黴素類抗菌藥，香港有 3 張注射劑型許可證。
TxGNN 模型預測它可能對**冠周炎 (Pericoronitis)** 有效。
目前**沒有臨床試驗**，相關的 20 篇文獻也**沒有直接測試 benzylpenicillin**，證據屬間接推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症 |
| 預測新適應症 | 冠周炎 (Pericoronitis) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L4（僅有機轉與間接研究，無直接臨床證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，benzylpenicillin 屬於青黴素類抗菌藥，對敏感細菌有殺菌作用。冠周炎是多種細菌混合造成的牙源性感染，機轉上可能適用。

冠周炎常見於智齒（尤其下顎）萌出不完全時，牙齦覆蓋部分牙冠而發炎。文獻指出其菌叢以厭氧菌為主，青黴素類（如 amoxicillin）與 metronidazole 被認為有效（PMID 1873287）。牙科抗生素的系統性回顧也建議，需使用抗生素時應先以 β-內醯胺類單一藥物治療（PMID 35959239）。

不過這個連結是間接的。本次沒有找到任何 benzylpenicillin 用於冠周炎的對照研究。2003 年的微生物研究還發現，下顎智齒冠周炎中有產 β-內醯胺酶的細菌（PMID 12789143），這可能限制未加酶抑制劑的青黴素效果。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻多數不是直接測試 benzylpenicillin 的研究。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39068391](https://pubmed.ncbi.nlm.nih.gov/39068391/) | 2024 | RCT（漱口水，非青黴素） | BMC oral health | 含 chlorhexidine、amoxicillin、metronidazole 等的複方漱口水用於急性冠周炎，評估疼痛與最大開口度 |
| [35959239](https://pubmed.ncbi.nlm.nih.gov/35959239/) | 2022 | 系統性回顧（metronidazole） | JAC-antimicrobial resistance | 牙科感染應在確有全身症狀時才用抗生素，首選 β-內醯胺類單一藥物 |
| [36268928](https://pubmed.ncbi.nlm.nih.gov/36268928/) | 2022 | Review | European journal of translational myology | 孕期牙髓治療的抗生素使用回顧 |
| [29693642](https://pubmed.ncbi.nlm.nih.gov/29693642/) | 2018 | Review | Antibiotics (Basel) | 兒童口顏面感染的抗生素處方，提醒牙科濫用抗生素的問題 |
| [26067725](https://pubmed.ncbi.nlm.nih.gov/26067725/) | 2015 | 回溯性世代研究 | J Contemp Dent Pract | 大學醫院牙科急診中牙源性感染的盛行率與處置 |
| [12789143](https://pubmed.ncbi.nlm.nih.gov/12789143/) | 2003 | 微生物研究 | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | 下顎智齒冠周炎中有產 β-內醯胺酶的細菌，可能影響青黴素效果 |
| [1873287](https://pubmed.ncbi.nlm.nih.gov/1873287/) | 1991 | 問卷調查 | Br J Oral Maxillofac Surg | 英國口腔顎面外科醫師認為青黴素類與 metronidazole 對急性冠周炎有效 |
| [40381916](https://pubmed.ncbi.nlm.nih.gov/40381916/) | 2025 | 監測研究 | J Infect Chemother | 日本牙源性感染分離菌的抗菌藥感受性監測 |
| [21027620](https://pubmed.ncbi.nlm.nih.gov/21027620/) | 1946 | 病例報告 | Am J Orthod Oral Surg | 以抽吸並灌注青黴素治療急性冠周炎引起的頜下膿瘍（年代久遠） |
| [14353202](https://pubmed.ncbi.nlm.nih.gov/14353202/) | 1954 | 歷史文獻 | Fogorvosi szemle | 以青黴素與 procaine 局部注射治療下顎智齒冠周炎（無摘要） |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-43500 | PAN-PENICILLIN G SOD FOR INJ 1M IU | DCH Auriga (Hong Kong) Limited - Universal Division |
| HK-60173 | NORAPENY FOR IM/IV INJ 1000000IU | Jindun Pharma (H.K.) Limited |
| HK-68195 | PENICILLIN G SODIUM SANDOZ POWDER FOR SOLUTION FOR INJECTION/INFUSION 1000000IU | Sandoz Hong Kong Limited |

三張許可證的品名都顯示為注射劑型（肌肉或靜脈注射），資料中沒有載明核准適應症與劑型欄位。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 冠周炎確實是抗菌藥常用的適應症，但沒有任何臨床試驗，也沒有直接測試 benzylpenicillin 的對照研究。
- 冠周炎多為局部、輕中度的感染，且可能有產 β-內醯胺酶的細菌，注射用青黴素 G 是否合適也存疑。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，這是目前的阻擋性資料缺口。
- 補充 benzylpenicillin 的作用機轉資料（可查詢 DrugBank）。
- 進行系統性文獻回顧，比較 benzylpenicillin 與現行標準用藥（amoxicillin、metronidazole）在冠周炎的療效，並評估注射劑型的必要性。
- 若要優先探索其他方向，預測排名第 3 的**口瘡（復發性口腔潰瘍）**已有 penicillin G 鉀含片的隨機對照試驗（PMID 33273940、14676759、20188604）。但這些研究用的是局部含片，與香港目前的注射劑型不同，且本次資料未提供其療效結果，仍需另行評估。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

