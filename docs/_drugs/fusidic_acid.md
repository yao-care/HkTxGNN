---
layout: default
title: Fusidic Acid
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
monitor_inn: "FUSIDIC ACID"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
last_modified_at: 2026-10-23
description: "Fusidic Acid：預測新適應症為暴露性角膜炎 (Exposure Keratitis)（證據等級 L5）。原適應症：知識圖譜記錄的關聯包括泌尿道感染、支氣管炎、痤瘡、毛囊炎等"
---

# Fusidic Acid
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

## Fusidic Acid：從細菌感染到暴露性角膜炎
{: .text-alpha }

## 一句話總結

Fusidic acid（夫西地酸）是一種抗生素，知識圖譜記錄的原有用途包括泌尿道感染、支氣管炎、痤瘡、毛囊炎等細菌相關疾病。
TxGNN 模型預測它可能對**暴露性角膜炎 (Exposure Keratitis)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇**間接相關的文獻（眼部 Tsukamurella 感染病例系列），證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯包括泌尿道感染、支氣管炎、痤瘡、毛囊炎等（本次資料中的香港許可證未附核准適應症文字） |
| 預測新適應症 | 暴露性角膜炎 (Exposure Keratitis) |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 核准數量 | 至少 20 張許可證（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理特性而言，fusidic acid 透過抑制細菌延長因子 EF-G 來阻斷蛋白質合成，對金黃色葡萄球菌等革蘭氏陽性菌有較強活性。香港有眼用黏稠滴眼液（FUCITHALMIC）的許可證，顯示眼表面細菌感染使用在生物學上說得通。

不過，暴露性角膜炎主要是眼瞼閉合不全造成的乾燥與機械性損傷，並非primarily 感染性疾病。抗菌藥物最多只能在併發繼發性細菌感染時發揮作用，不能處理疾病的根本原因。

所附唯一文獻是 Tsukamurella 菌屬眼部感染的病例系列，並未研究 fusidic acid，也未針對暴露性角膜炎，因此無法直接支持這項預測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | 病例系列 | Cornea | 描述 Tsukamurella 菌屬所致眼部感染的臨床表現、風險因子、治療與預後，並首次報告摘除眼球後植入物感染；未涉及 fusidic acid 或暴露性角膜炎 |

## 香港上市資訊

以下為資料中列出的部分許可證（清單可能不完整，總數至少 20 張）。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60364 | FULOSIN CREAM 2% | WINGS PHARMACEUTICAL LTD |
| HK-46825 | FOBAN CREAM 2% | TAISHO PHARMACEUTICAL (HK) LTD |
| HK-65120 | DEFUZIN CREAM 2% W/W | FP HEALTHCARE LIMITED |
| HK-37408 | FUCIDIN CREAM 2% | DKSH HONG KONG LIMITED |
| HK-37597 | FUCITHALMIC VISCOUS EYE DROPS 10MG/G | AMDIPHARM MERCURY (HONG KONG) LIMITED |

另有口服懸浮用乾粉劑（PHUDICIN DRY SUSP 250MG/SACHET，HK-55629）等其他單方許可證。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容，僅供參考）：肝衰竭、腎臟疾病、肝病、膽囊疾病、單純皰疹病毒角膜炎、青光眼、眼部感染性疾病、結膜炎、糖尿病、心房顫動、重症肌無力、艱難梭菌結腸炎、呼吸衰竭等。其中與眼部相關的項目（單純皰疹病毒角膜炎、青光眼、高眼壓、眼部感染性疾病、結膜炎）在評估眼用途徑時需特別留意。

其餘警語、禁忌與藥物交互作用資料目前缺乏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，唯一文獻未直接研究暴露性角膜炎與 fusidic acid，故證據等級僅為 L5，預測僅來自模型。
- 暴露性角膜炎主要是機械性／乾燥性疾病，抗菌作用僅適用於繼發感染，機轉上的契合度有限。

**若要推進需要：**
- 取得 fusidic acid 的作用機轉與仿單警語／禁忌資料（目前為阻擋性資料缺口）
- 搜尋並評估 fusidic acid 用於角膜或眼表疾病（含繼發細菌感染）的直接研究
- 確認眼用劑型的核准適應症與安全性，並釐清暴露性角膜炎中是否有明確的抗菌使用情境
- 評估葡萄球菌對 fusidic acid 的抗藥性風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

