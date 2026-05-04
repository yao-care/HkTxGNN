---
layout: default
title: Dornase Alfa
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Dornase Alfa
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

# Dornase alfa：從囊性纖維化到腺泡型前列腺黏液性腺癌

## 一句話總結

Dornase alfa 是一種重組人類去氧核糖核酸酶 I（rhDNase），原本用於囊性纖維化（Cystic Fibrosis）的肺部黏液清除治療。
TxGNN 模型預測它可能對**腺泡型前列腺黏液性腺癌 (Acinar Prostate Mucinous Adenocarcinoma)** 有效，
但目前**無任何臨床試驗或文獻**支持此新適應症預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 囊性纖維化（香港監管資料無核准記錄，依藥理學已知用途） |
| 預測新適應症 | 腺泡型前列腺黏液性腺癌 (Acinar Prostate Mucinous Adenocarcinoma) |
| TxGNN 預測分數 | 50.00%（知識圖譜排名 #1,784,502） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理，Dornase alfa 是一種重組人類 DNase I 酵素，透過降解黏稠痰液中的胞外 DNA 來改善囊性纖維化患者的肺部清除功能。

從機轉角度推測，Dornase alfa 的 DNase 活性理論上可降解腫瘤微環境中由中性粒細胞胞外陷阱（NETs）釋放的胞外 DNA，進而調節腫瘤免疫微環境。此外，黏液性腺癌富含黏液的特性與 CF 黏液清除的機轉存在遠端類比。

然而，**這條機轉推測鏈極度薄弱**：腺泡型前列腺黏液性腺癌是一種罕見且高度特化的腫瘤亞型，目前完全缺乏任何前臨床或臨床資料支持 Dornase alfa 在此疾病的應用。TxGNN 排名 #1,784,502 亦顯示此預測為低信心輸出。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Dornase alfa 目前在香港**尚未取得上市許可**，無任何已核准的藥品許可證記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有 10 項 TxGNN 預測均為 L5 證據等級（僅模型預測，無實際研究），且排名均超過 #1,784,000，顯示預測信心極低。
- Dornase alfa 在香港未有上市記錄，缺乏監管基礎，且首要預測適應症（腺泡型前列腺黏液性腺癌）在機轉、前臨床及臨床層面均無任何支持數據。

**若要推進需要：**
- 補全 Dornase alfa 的完整作用機轉（MOA）資料（建議查詢 DrugBank API）
- 補全香港上市安全性資料（警語、禁忌症、仿單）
- 先評估與已知適應症（CF）生物學距離較近的疾病（如其他黏液分泌異常相關疾病、NETs 相關炎症性疾病），而非直接跨越至罕見癌症亞型
- 若仍有興趣探索腫瘤應用，需先取得 DNase / NETs 軸在前列腺黏液性腺癌的前臨床概念驗證（PoC）數據

---

> ⚠️ **免責聲明**：本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過嚴格臨床驗證方可應用於臨床。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

