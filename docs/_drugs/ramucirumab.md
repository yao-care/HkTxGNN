---
layout: default
title: Ramucirumab
parent: 僅模型預測 (L5)
nav_order: 631
evidence_level: L5
indication_count: 10
---

# Ramucirumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ramucirumab：從晚期實體腫瘤到子宮韌帶腺癌

## 一句話總結

Ramucirumab 是抗 VEGFR2 單株抗體，其抗血管新生機轉已在胃癌、非小細胞肺癌、大腸直腸癌、肝細胞癌等實體腫瘤獲得驗證。TxGNN 模型預測它可能對**子宮韌帶腺癌 (Uterine Ligament Adenocarcinoma)** 及其他 9 種婦科罕見腺癌亞型有效，但目前**無任何臨床試驗登記、無文獻報告**，純屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺乏（香港未上市，無許可證核准適應症文字；已知全球用於胃癌、NSCLC、大腸直腸癌、HCC 等實體腫瘤） |
| 預測新適應症 | 子宮韌帶腺癌 (Uterine Ligament Adenocarcinoma) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Ramucirumab 為抗 VEGFR2（KDR）單株抗體，透過阻斷腫瘤血管新生產生抗腫瘤效果，此機轉已在胃癌、非小細胞肺癌、大腸直腸癌、肝細胞癌等多種實體腫瘤獲得臨床驗證。

子宮韌帶腺癌屬於婦科罕見腫瘤，理論上實體腫瘤的血管新生依賴性可能同樣存在，因此 VEGFR2 阻斷機轉在理論上可能適用。但這僅為機轉層次的推論延伸——目前無任何 ramucirumab 用於該亞型（或其他 9 個相近婦科罕見腺癌亞型）的臨床試驗或文獻報告，query_log 中所有相關檢索（ClinicalTrials.gov、ICTRP、PubMed）皆為 0 筆結果。

值得注意的是，10 個預測候選中排名第 10 的「腸型子宮頸黏液腺癌」因組織學上與大腸直腸腺癌相似，而 ramucirumab 已核准用於大腸直腸癌，是唯一具間接機轉類比支持的候選；其餘候選（含排名第一的子宮韌帶腺癌）皆缺乏此類間接佐證，機轉合理性相對較弱。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Ramucirumab 目前未於香港上市，無許可證資料。

## 細胞毒性（標靶抗腫瘤藥物）

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗血管新生單株抗體，VEGFR2 拮抗劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本評估報告中的 TFDA 仿單警語/禁忌資料為 Blocking 等級缺口（DG001），在補齊前無法進入 S1 安全性初評階段。

## 其他候選適應症（TxGNN 高分預測，均為 L5／Hold）

| 排名 | 疾病 | TxGNN 分數 | 證據狀態 |
|------|------|-----------|---------|
| 2 | Endocervical carcinoma | 99.95% | 無臨床試驗/文獻 |
| 3 | Adenoid cystic carcinoma of the cervix uteri | 99.95% | 無臨床試驗/文獻 |
| 4 | Uterine ligament serous adenocarcinoma | 99.94% | 無臨床試驗/文獻 |
| 5 | Signet ring cell variant cervical mucinous adenocarcinoma | 99.94% | 無臨床試驗/文獻 |
| 6 | Cervical adenosquamous carcinoma, glassy cell variant | 99.94% | 無臨床試驗/文獻 |
| 7 | Uterine ligament endometrioid adenocarcinoma | 99.94% | 無臨床試驗/文獻 |
| 8 | Uterine ligament clear cell adenocarcinoma | 99.94% | 無臨床試驗/文獻 |
| 9 | Uterine ligament mucinous adenocarcinoma | 99.94% | 無臨床試驗/文獻 |
| 10 | Intestinal variant cervical mucinous adenocarcinoma | 99.94% | 無臨床試驗/文獻（唯一有間接機轉類比：CRC 已核准適應症） |

## 結論與下一步

**決策：Hold**

**理由：**
10 個預測候選適應症全數為 L5 等級（僅有 TxGNN 模型分數，無任何臨床試驗或文獻支持），且香港未上市、無許可證資料，同時存在 Blocking 等級的仿單警語資料缺口，尚無法評估安全性。

**若要推進需要：**
- 補齊 TFDA/藥品仿單的警語與禁忌症資料（DG001，Blocking）
- 透過 DrugBank API 查詢完整作用機轉資料（DG002，High）
- 針對排名前 3 的候選適應症進行系統性文獻與試驗登記庫再檢索，確認是否有近期新增證據
- 若無法取得直接證據，應優先評估與 CRC 有組織學類比性的候選（排名 10）作為機轉驗證起點
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

