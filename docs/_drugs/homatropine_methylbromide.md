---
layout: default
title: Homatropine Methylbromide
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 2
---

# Homatropine Methylbromide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Homatropine Methylbromide：從腸胃痙攣到胃十二指腸炎

## 一句話總結

Homatropine Methylbromide 是一種四級銨鹽類抗膽鹼劑，傳統用於消化性潰瘍及腸胃痙攣的症狀緩解。
TxGNN 模型預測它可能對**胃十二指腸炎 (Gastroduodenitis)** 有效，
目前**無臨床試驗**及**無文獻**支持這個方向，屬於純模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腸胃痙攣／消化性潰瘍（抗膽鹼劑藥理分類） |
| 預測新適應症 | 胃十二指腸炎 (Gastroduodenitis) |
| TxGNN 預測分數 | 99.39% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Homatropine Methylbromide 為四級銨鹽類抗膽鹼劑，可拮抗 M1、M2、M3 毒蕈鹼受體。因帶有四級銨結構，不穿越血腦屏障，作用局限於周邊自主神經系統，傳統適應症為消化性潰瘍與腸胃痙攣。

胃十二指腸炎（Gastroduodenitis）為胃與十二指腸黏膜同時發炎，常見原因為 *Helicobacter pylori* 感染、NSAID 藥物損傷或過多胃酸。就症狀管理層面，M1 受體拮抗可抑制胃酸分泌，M3 受體拮抗可鬆弛腸胃平滑肌痙攣，機轉上存在一定間接合理性。

然而，胃十二指腸炎的核心病因（細菌感染或黏膜損傷）並非抗膽鹼劑的主要作用對象。現行標準治療以抗生素根除 *H. pylori* 或質子幫浦抑制劑（PPI）為主，抗膽鹼劑至多為輔助症狀緩解。TxGNN 的預測很可能來自知識圖譜中「胃酸過多」與「平滑肌痙攣」節點的間接連結，屬於間接類推，而非直接針對炎症病因。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

此藥物目前在香港**未取得上市許可**，無許可證資料可查。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
本案僅有 TxGNN 模型預測（L5），無任何臨床試驗或文獻佐證；胃十二指腸炎的核心病因為感染或黏膜損傷，抗膽鹼劑的機轉合理性屬間接推論，且藥物在香港尚未取得上市許可，進入評估的基礎條件不足。

**若要推進需要：**
- 補充 MOA 詳細資料（查詢 DrugBank API，填補 DG002 缺口）
- 補充安全性警語與禁忌症（下載原廠仿單 PDF 解析，填補 DG001 缺口）
- 搜尋 *H. pylori* 相關或胃炎輔助治療的前臨床研究，確認是否存在 L4 等級以上證據
- 評估香港申請許可證（NDA）的法規可行性，作為後續在地化佈局依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

