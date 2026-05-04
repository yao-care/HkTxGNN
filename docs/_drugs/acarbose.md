---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acarbose：從糖尿病到局灶性僵肢症候群

## 一句話總結

Acarbose 是一種口服降糖藥，透過抑制腸道 α-葡萄糖苷酶來延緩碳水化合物吸收，主要用於第 2 型糖尿病的餐後血糖管理。
TxGNN 模型預測它可能對**局灶性僵肢症候群 (Focal Stiff Limb Syndrome)** 有效，
但目前**無臨床試驗**、**無直接文獻**支持此方向，預測連結屬純計算推斷層面。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病（餐後高血糖管理） |
| 預測新適應症 | 局灶性僵肢症候群 (Focal Stiff Limb Syndrome) |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Acarbose 是一種 α-葡萄糖苷酶抑制劑，透過延緩腸道碳水化合物的酶解與吸收，降低餐後血糖峰值，廣泛用於第 2 型糖尿病管理。其作用局限於消化道，不直接影響中樞神經系統。

局灶性僵肢症候群（Focal Stiff Limb Syndrome）是僵人症候群（Stiff Person Syndrome, SPS）的亞型，主要病理機制為抗 GAD65 抗體攻擊 GABAergic 神經元，導致局部肌肉僵硬與痙攣。關鍵的生物學共點在於：GAD65（麩胺酸脫羧酶 65）同時也是第 1 型糖尿病的核心自身抗原，SPS 患者合併糖尿病的盛行率高達 30–40%。

TxGNN 模型可能透過此「GAD65 共享自身抗原共病網路」建立計算連結，推斷 Acarbose 對 SPS 合併糖尿病患者的血糖管理具輔助角色。然而，Acarbose 對 GABAergic 神經元保護並無直接機轉，對 SPS 核心病理（GABA 缺乏、肌肉僵硬）亦無已知干預途徑，目前的連結仍屬計算推斷層面，缺乏任何臨床前或臨床數據支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有 TxGNN 模型的計算預測（L5 等級），機轉連結屬間接共病推斷，Acarbose 對局灶性僵肢症候群的核心病理（GABA 系統失調）無已知直接干預機制；藥物在香港亦尚未上市，欠缺任何臨床前或臨床研究支持。

**若要推進需要：**
- 完整 MOA 資料（查詢 DrugBank API，補充 DG002 資料缺口）
- 安全性仿單分析（TFDA 或原廠仿單 PDF 解析，補充 DG001 資料缺口）
- 針對 SPS 合併糖尿病患者進行文獻回顧，確認 Acarbose 等 α-葡萄糖苷酶抑制劑在此族群的臨床應用紀錄
- 香港上市可行性評估（進口藥品申請途徑）
- 如擬升級至 L4，需有至少一項 Acarbose 與 GAD65 自身免疫路徑相關的臨床前研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

