---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
monitor_inn: "CEFTAZIDIME"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "urinary tract infection (disease)", "epiglottitis", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "infectious otitis media", "Peptostreptococcus infectious disease"]
last_modified_at: 2026-10-23
description: "Ceftazidime：預測新適應症為多株性高黏滯症候群（證據等級 L5）。原適應症：本地許可證資料未載明核准適應症。知識圖譜記錄的相關關係包括鏈球菌感染、細菌性肺炎、腹膜炎、細菌性腦膜炎、金黃色葡萄球菌感染、大腸桿菌感染等"
---

# Ceftazidime
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Ceftazidime：從細菌感染到多株性高黏滯症候群
{: .text-alpha }

## 一句話總結

Ceftazidime（頭孢他啶）是第三代頭孢子菌素類注射抗生素，知識圖譜記錄的相關用途以各類細菌感染為主。
TxGNN 模型預測它可能對**多株性高黏滯症候群 (polyclonal hyperviscosity syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未載明核准適應症。知識圖譜記錄的相關關係包括鏈球菌感染、細菌性肺炎、腹膜炎、細菌性腦膜炎、金黃色葡萄球菌感染、大腸桿菌感染等（僅為知識圖譜關係，並非許可證核准適應症） |
| 預測新適應症 | 多株性高黏滯症候群 |
| TxGNN 預測分數 | 0.9951 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ceftazidime 一般認為是透過結合細菌的青黴素結合蛋白（PBP），抑制細胞壁合成而殺菌，屬於抗細菌藥物。

多株性高黏滯症候群是免疫球蛋白過多造成血液黏滯度上升的病況，不是感染性疾病。抗菌藥物的機轉與這個疾病之間沒有合理的生物學連結。這個高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 8 張有效許可證，以下列出 5 張單一成分許可證。資料中未記錄劑型與核准適應症文字，因此無法由許可證確認本藥在香港的核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-21523 | FORTUM FOR INJ 2G | SANDOZ HONG KONG LIMITED |
| HK-21522 | FORTUM FOR INJ 500MG | SANDOZ HONG KONG LIMITED |
| HK-21251 | FORTUM FOR INJ 1G | SANDOZ HONG KONG LIMITED |
| HK-57297 | CEFTAZIDIME FOR INJ 1G (REYOUNG) | JINDUN PHARMA (H.K.) LIMITED |
| HK-61251 | CEFTAZIDIME POWDER FOR SOLUTION FOR INJECTION 2G | CEUTICAL TRADING COMPANY LIMITED |

另有一張 ZAVICEFTA（ceftazidime 與 avibactam 複方）許可證，不能用來說明單一成分 ceftazidime 的核准或上市情形。

## 安全性考量

- **知識圖譜記錄的禁忌關係**（非仿單文字）：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、凝血功能疾病、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、先天性凝血酶原缺乏。
- **藥物交互作用**：共查得 100 筆。中度交互作用包括 Amphotericin B（含各種劑型）、Kanamycin、Neomycin、Streptomycin 與 Picosulfuric acid。

仿單的主要警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測沒有任何臨床或文獻證據，機轉上也缺乏合理性，應視為模型的網路假象。
- 證據等級為 L5，不建議投入資源。

**若要推進需要：**
- 取得 Ceftazidime 的作用機轉資料，並檢視與免疫球蛋白或血液黏滯度相關的生物學依據。
- 取得香港仿單中的警語與禁忌症。
- 提出具體的生物學假說，並進行前臨床驗證。

**補充說明：** 同一份預測清單中，**泌尿道感染**（分數 0.9941）有較多證據，包括已完成的 Phase 2 隨機試驗（NCT00921024）與 Phase 4 研究（NCT04882085）。但這些試驗主要涉及頭孢他啶與抗藥性抑制劑的複方，不等同於單一成分的證據。**感染性中耳炎**則有兒童慢性化膿性中耳炎的小型研究。這兩項都比本報告的主要預測更值得優先評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

