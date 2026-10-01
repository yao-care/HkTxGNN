---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 495
evidence_level: L5
indication_count: 5
---

# Lactulose
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

# Lactulose：從原適應症（資料未載明）到急性尿酸腎病變

## 一句話總結

Lactulose 是一種不被吸收的雙醣類藥物，香港已有多張許可證，但本次資料未載明其核准適應症。
TxGNN 模型預測它可能對**急性尿酸腎病變 (Acute Urate Nephropathy)** 有效。
目前**沒有臨床試驗和文獻**支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 急性尿酸腎病變 (Acute Urate Nephropathy) |
| TxGNN 預測分數 | 99.89%（模型排名 2,852） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，也沒有原適應症資料可供比對。根據已知資訊，lactulose 是不被吸收的雙醣類，臨床上常用於肝性腦病變。但現有資料無法建立它與急性尿酸腎病變之間的機轉連結。

TxGNN 給出的分數很高（99.89%），但這只是知識圖譜的模型推論。既沒有試驗或文獻佐證，也沒有機轉資料，所以目前只能視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 13 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-43381 | PMS-LACTULOSE SOLUTION 667MG/ML | Trenton-Boma Ltd |
| HK-67979 | LALALAX ORAL SOLUTION 10G/15ML | FP Healthcare Limited |
| HK-68911 | LOLAN ORAL SOLUTION 66.7G/100ML | Healthcare Pharmascience Limited |
| HK-68890 | BF-LACTULOSE ORAL SOLUTION 667MG/ML | Bright Future Pharmaceuticals Factory |
| HK-67881 | CONSIQARE ORAL SOLUTION 667MG/ML | FP Healthcare Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
首位預測（急性尿酸腎病變）的證據等級為 L5，沒有任何試驗或文獻，也缺乏作用機轉資料，不足以推進。

**其他預測適應症供參考：**

| 排名 | 預測適應症 | 分數 | 證據等級 | 決策 |
|------|-----------|------|---------|------|
| 2 | 腎結石 (Nephrolithiasis) | 99.78% | L5 | Hold |
| 3 | 阻塞性黃疸 (Obstructive Jaundice) | 99.53% | L3 | Research Question |
| 4 | 膽管疾病 (Bile Duct Disease) | 99.47% | L4 | Hold |
| 5 | 膽道疾病 (Biliary Tract Disease) | 99.38% | L4 | Hold |

其中**阻塞性黃疸**是證據最多的方向，有 1 個 Phase 4 試驗（NCT01090193，n=20，但未以 lactulose 為介入措施）和約 20 篇文獻。多篇文獻直接探討 lactulose 在此情境下的作用（例如 PMID 3768644、12957136、2032107），假說是減少腸道內毒素吸收與細菌移位，進而降低術後腎功能不全風險。但現有證據多為動物研究或較舊的小型臨床研究，設計與結果無法僅從標題確認，也未見 Phase 3 RCT。

**若要推進需要：**
- 補齊 lactulose 的作用機轉資料（DrugBank）
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選
- 針對急性尿酸腎病變做專門的文獻與試驗檢索
- 確認各張許可證的核准適應症與劑型
- 若優先考慮阻塞性黃疸，需逐篇確認 PMID 2032107、3768644 等研究的設計與結果

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

