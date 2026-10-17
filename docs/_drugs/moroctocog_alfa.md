---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 598
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Moroctocog Alfa：預測新適應症為原發性血小板釋放障礙 (primary release disorder of platelets)（證據等級 L5）。原適應症：血友病（hemophilia）、女性帶因者的症狀性血友病"
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome"]
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Moroctocog alfa：從血友病到原發性血小板釋放障礙

## 一句話總結

Moroctocog alfa 是重組人類凝血因子 VIII（去除 B 結構域），原本用於血友病治療。
TxGNN 模型預測它可能對**原發性血小板釋放障礙 (primary release disorder of platelets)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測，機轉上也缺乏合理依據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血友病（hemophilia）、女性帶因者的症狀性血友病（資料來源為知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 原發性血小板釋放障礙 (primary release disorder of platelets) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Moroctocog alfa 是重組凝血因子 VIII（B 結構域去除型），用於補充血友病患者缺乏的 FVIII，其療效在血友病中已被確立。

然而，原發性血小板釋放障礙（血小板儲存池／分泌缺陷）是血小板本身的功能異常，並非 FVIII 缺乏。補充 FVIII 預期無法矯正這項缺陷。TxGNN 的高分較可能反映出血性疾病在知識圖譜中的鄰近關係，而非實際的機轉關聯。因此這項預測的合理性偏低。

**其他預測適應症（同樣皆為 L5、Hold）：**

| 排名 | 預測適應症 | TxGNN 分數 | 機轉評估 |
|------|-----------|-----------|---------|
| 2 | 假性血管性血友病 (pseudo-von Willebrand disease) | 99.97% | 病因為血小板 GP1BA 功能獲得性變異，與 FVIII 補充的關聯弱且間接；通常以血小板輸注治療 |
| 3 | Glanzmann 血小板無力症 (Glanzmann thrombasthenia) | 99.96% | 缺陷在整合素 αIIbβ3，FVIII 無法矯正；標準治療為血小板輸注、抗纖溶藥物與重組 FVIIa |
| 4 | 後天性凝血因子缺乏 (acquired coagulation factor deficiency) | 99.88% | 五者中生物學上最合理，理論上可補充後天性 FVIII 缺乏。但後天性血友病 A 由自體抗體介導，會中和輸注的 FVIII，標準治療為旁路製劑；且此類別異質性高（如維生素 K 缺乏、肝病、DIC），單一因子補充並不適當 |
| 5 | Scott 症候群 (Scott syndrome) | 99.86% | 缺陷在磷脂絲胺酸暴露（TMEM16F/ANO6 變異），FVIII 水平正常，補充無助益 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66835 | XYNTHA POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 250IU | 注射用粉劑及溶劑 | 未載明 |
| HK-66834 | XYNTHA POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 1000IU | 注射用粉劑及溶劑 | 未載明 |
| HK-66836 | XYNTHA POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 500IU | 注射用粉劑及溶劑 | 未載明 |

三張許可證皆為單一成分、現行有效，持證商為 Pfizer Corporation Hong Kong Limited。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 五個預測適應症皆只有模型分數，沒有臨床試驗或文獻支持（L5）。
- 這些疾病多為血小板功能缺陷，與 FVIII 補充缺乏機轉關聯。唯一較合理的「後天性凝血因子缺乏」，也因抑制物中和與病因異質性而不適合直接套用。

**若要推進需要：**
- 取得並解析香港衛生署核准仿單，確認警語、禁忌與核准適應症。
- 補充詳細的作用機轉資料（MOA）。
- 若要探索，應聚焦於「後天性凝血因子缺乏」中明確的 FVIII 缺乏亞型，並做文獻回顧與臨床專家評估。
- 其餘四項血小板疾病建議不優先投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

