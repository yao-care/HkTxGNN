---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 5
---

# Etravirine
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

# Etravirine：從 HIV-1 感染到貓後天免疫缺乏症候群

## 一句話總結

Etravirine（依曲韋林）是第二代非核苷逆轉錄酶抑制劑（NNRTI），原本用於治療 HIV-1 感染（含多種耐藥突變株）。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群（Feline Acquired Immunodeficiency Syndrome）**有效，
然而目前**無任何臨床試驗**或**相關文獻**支持此方向，且此適應症屬獸醫領域，超出人用再利用核心範疇。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（香港未上市） |
| 預測新適應症 | 貓後天免疫缺乏症候群（Feline Acquired Immunodeficiency Syndrome） |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Etravirine 屬於二芳嘧啶類（DAPY）NNRTI，透過非競爭性結合 HIV-1 逆轉錄酶（RT）的疏水性口袋（β12–β13–β14 三葉草區域），阻斷 RNA 依賴性 DNA 合成，從而抑制 HIV-1 病毒複製。相較於第一代 NNRTI，Etravirine 採「彈性結合」構型，對多種耐藥突變株（如 K103N、Y181C）仍保有活性。

貓後天免疫缺乏症候群（由 FIV 引起）與 HIV-1 感染同屬逆轉錄病毒科慢病毒屬，在知識圖譜中節點高度鄰近，是 TxGNN 給出 99.98% 高分的推測原因。然而，NNRTI 的結合位點高度依賴 HIV-1 RT 的特異性三維結構；FIV RT 與 HIV-1 RT 序列差異顯著，既有研究顯示古典 NNRTI（nevirapine、efavirenz）對 FIV 幾乎無效，目前也完全無針對 FIV 的 Etravirine 體外或臨床數據。

綜合來看，此預測最可能為知識圖譜鄰近性驅動的算法結果，而非真實藥物活性的反映。加之貓 AIDS 屬獸醫疾病，並非人用藥物再利用的目標範疇，機轉合理性存疑。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Etravirine 在香港尚未取得藥物許可證，無上市記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
首要預測適應症（貓後天免疫缺乏症候群）屬獸醫疾病，既無人用先例，亦無任何體外或臨床數據支持 Etravirine 對 FIV 的實際活性，機轉合理性有限。此高分預測屬知識圖譜拓撲偽陽性的典型案例。

值得注意的是，Evidence Pack 中排名第 4（AIDS 相關複合症，Score 99.79%）與第 5（先天性 HIV，Score 99.79%）的預測具有更強的臨床轉化潛力——兩者均為 HIV-1 疾病谱，與 Etravirine 已核准適應症機轉完全一致，且兒科擴展使用（PIANO 研究）已有初步文獻支持，值得優先評估。

**若要推進需要：**
- 重新選定評估目標：建議排除獸醫疾病，將 AIDS 相關複合症（Rank 4）與先天性 HIV（Rank 5）列為優先候選
- 補充作用機轉資料（DG002）：查詢 DrugBank API 取得完整 MOA 描述
- 補充安全性資訊（DG001）：取得仿單警語、禁忌症及藥物交互作用資料
- 針對先天性 HIV（Rank 5），確認 PIANO 研究及 FDA 兒科核准（6 歲以上）的完整文獻，評估香港申請許可的可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

