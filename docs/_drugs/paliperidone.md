---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 645
evidence_level: L5
indication_count: 5
---

# Paliperidone
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

# Paliperidone：從抗精神病用途到視網膜失養症（預測）

## 一句話總結

Paliperidone 是非典型抗精神病藥，在香港已有多張上市許可證。
TxGNN 模型預測它可能對**視網膜失養症（伴或不伴眼外異常）**有效，
但目前**沒有臨床試驗**，檢索到的 **15 篇文獻**也與本藥無直接關聯，實質證據不足。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 視網膜失養症，伴或不伴眼外異常 (retinal dystrophy with or without extraocular anomalies) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Paliperidone 屬於非典型抗精神病藥，一般認為作用於 D2 與 5-HT2A 受體拮抗，但此點並非來自完整的 MOA 資料。

我們未找到合理的機轉連結。視網膜失養症多屬遺傳性視網膜病變，沒有已知的途徑讓 D2/5-HT2A 拮抗劑改變其病程。0.999 的高分只是知識圖譜的預測，不代表有生物學或臨床依據。

另外兩個近視相關預測（X 連鎖近視、症候群性近視）可能透過視網膜多巴胺訊號連結，但 D2 拮抗在動物模型中傾向促進而非減緩近視，方向可能不利。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下 15 篇文獻中，依 RCT > Review > Case report 列出前 10 篇。其中**沒有 RCT**。從標題判斷，這些文獻都沒有討論 paliperidone 或視網膜失養症的治療，應是僅以疾病關鍵字比對而來，因此**不能視為支持證據**。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | 眼眶感染的成因與影像表現 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | 複視的臨床評估方法 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | 先天性眼瞼下垂的類型與處置 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | 先天性水晶體形狀異常 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler 症候群的玻璃體視網膜病變 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | 兒童眼眶病變的鑑別診斷與影像 |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Arch Ophthalmol | 眼眶動靜脈畸形的臨床表現與預後 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | 單側隱眼症病例 |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | J Neuroophthalmol | 先天性滑車神經—動眼神經聯合運動 |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optom Vis Sci | 先天性眼外肌纖維化的協同性外斜視 |

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68512 | COMPASSIA PROLONGED-RELEASE SUSPENSION FOR INJECTION IN PRE-FILLED SYRINGE 50MG/0.5ML | ABBOTT LAB LTD |
| HK-56192 | INVEGA EXTENDED-RELEASE TAB 3MG | JOHNSON & JOHNSON (HONG KONG) LTD. |
| HK-60142 | INVEGA SUSTENNA PROLONGED RELEASE SUSP FOR IM INJ. 100MG | JOHNSON & JOHNSON (HONG KONG) LTD. |
| HK-66467 | PAMOPREX PROLONGED-RELEASE TABLETS 6MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-66867 | PALIPERIDONE EXTENDED-RELEASE TABLETS 6MG | HONG KONG MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自知識圖譜（L5），沒有臨床試驗，檢索到的文獻也與本藥無關。
- 機轉上找不到合理連結，其他四個預測（近視兩項、無腦水腫、糖基化先天異常）同樣缺乏證據，且多屬遺傳或結構性疾病。

**若要推進需要：**
- 取得完整的作用機轉資料（DrugBank），評估是否存在可信的機轉連結
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩檢
- 以 paliperidone 與視網膜相關疾病為主題，重新做精準文獻檢索，並檢查是否有前臨床研究
- 在上述缺口補齊、出現實質證據之前，不建議投入資源

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

